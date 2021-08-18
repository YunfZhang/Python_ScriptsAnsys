#! /usr/bin/perl -w -I/home/grandpas/pro/cs/lib
# replace with your installation settings

use strict;
use Getopt::Long;
use ChangeSynergy::csapi;
use Time::gmtime;

# Usage: get_report.pl [-f format] query attributes
# This script is gpl'ed. See www.fsf.org.

my $usage = <<EOU;
usage: $0 [-h] [-f format ] [-q query] [-d database] attributes

$0 displays a text report with specified attributes;

The records to retrieve are either specified on stdin or 
directly specified with a query string. 

If a format string is provided (classic printf C format) 
attributes will follow String format.

If database is not provided, PR_SCADE is use by default

$0 -f "[%s] %s|%s|%s" -q "(software match 'good*')" problem_number

Attributes can be:
-problem_number
-problem_synopsis
-problem_description
-severity
-problem_synopsis
-software_platform
-software_version

[12990] search fails|embedded|2.3
[14851] generated html does not validate|server|2.1
[14928] dead links|server|2.1

EOU
die $usage if ($#ARGV == -1);

Getopt::Long::Configure("bundling");

#Set to 1 to user "validation" user
my $dflt_user=1;

# Set accordingly to your installation
my $SERV_IP = "192.168.3.10";
my $SERV_DB = "/data/ccmdb/PR_SCADE";
my ($USER_LOGIN,$USER_PASSWD);
if ($dflt_user==1) {
	#Default user#
	$USER_LOGIN = "validation_reader";
	$USER_PASSWD = "validation";
} else {
	$USER_LOGIN = "thuong";
	$USER_PASSWD = get_pwd();
}
my $USER_ROLE = "User";

# Variables declaration
my ($user, $results,
    $queryargs, $querystring, 
    $opt_query, $opt_help, 
    $opt_format,$opt_db,
    $identifier, @identifiers);

# Define available options
my $options = GetOptions( 'q|query=s' => \$opt_query,
  'h|help' => \$opt_help, 'f|format:s' => \$opt_format, 'd|database:s' => \$opt_db);

die $usage if (defined($opt_help));

# If no query is furnished, build a query to retrieve 
# needed attributes from problem_number given as std 
# input.
if (defined($opt_query)) { $querystring = $opt_query; }
else {
  while (<STDIN>) {
    chomp;
    push @identifiers, $_;
  }
  $identifier = pop @identifiers;
  $querystring = qq/(problem_number='$identifier')/;
  foreach $identifier (@identifiers) {
    $querystring = $querystring . qq/or(problem_number='$identifier')/;
  }
}
    
eval
{
  $queryargs = join "|", @ARGV;
  

  if (defined($opt_db)) {
	$SERV_DB = "/data/ccmdb/".$opt_db;
  }
  
  my $csapi = new ChangeSynergy::csapi();
  $csapi->setUpConnection("http", $SERV_IP, 8600);
  $user = $csapi->Login($USER_LOGIN, $USER_PASSWD, 
                        $USER_ROLE, $SERV_DB);

  # Get query data
  $results = $csapi->QueryData($user, "Basic Summary", 
     $querystring, undef, undef, undef, $queryargs);
};

if ($@)
{
  print $@;
  print "No match. Dying. \n";
  exit 64;
}  

# Loop through the results to display formatted attributes
for (my $i = 0 ; $i < $results->getDataSize() ; $i++) {
  my $report_data = $results->getDataObject($i);
  my @attribute_data;
  my $finalattr;


  for (my $j = 0 ; $j < $report_data->getDataSize() ; $j++) {
    # converts universal time since epoch to modern styles.
    if ($report_data->getDataObject($j)->getType() eq "CCM_DATE") {
      my $gm = gmtime($report_data->getDataObject($j)->getValue());
      $attribute_data[$j] = sprintf "%2.2d%2.2d%2.2d", 
          $gm->year-100, $gm->mon+1, $gm->mday+1;
    } else {
      $attribute_data[$j] = $report_data->getDataObject($j)->getValue();
    }
  }
  if (defined($opt_format)) {
    $finalattr = sprintf $opt_format, @attribute_data;
  } else {
    $finalattr = join "|", @attribute_data;
  }
  print "$finalattr \n";
}


sub get_pwd { #read password saved in password.txt and encrypted thanks to encrypt.pl

my @salt = ( '.', '/', 0 .. 9, 'A' .. 'Z', 'a' .. 'z','.', '/', 0 .. 9, 'A' .. 'Z', 'a' .. 'z' ); 
push(@salt, '.', '/', 0 .. 9, 'A' .. 'Z', 'a' .. 'z','.', '/', 0 .. 9, 'A' .. 'Z', 'a' .. 'z' );
my %hash; foreach(0..scalar @salt/2-1) { $hash{$salt[$_]}=$_;}

chomp(my $pwd=`cat password.txt`); #encrypted password
chomp (my $key=`hostname`);

my @words=split(//,$pwd); my $size_pwd=scalar @words; 
my @keys=split(//,$key);

if ($size_pwd>@keys) {
	foreach (1..$size_pwd/@keys) { push (@keys,split(//,$key)); }
}

my $decrypted;
foreach my $i (0..$size_pwd-1) {
	$decrypted.=$salt[$hash{$words[$i]}-$hash{$keys[$i]}];
}

return $decrypted;
}

__END__

=pod

=head1 Name

B<getreport.pl> -- Displays specified fields from 
a selection of problem reports.

=head1 Synopsis

Usage: B<getreport.pl> [-h] [-f format ] [-q query] attributes

=head1 Description

$0 displays a text report with specified attributes;

The records to retrieve are either read on stdin
or directly specified with a query string. 

If a format string is provided (classic printf C 
format) attributes will follow String format.

$0 -f "[%s] %s|%s|%s" -q "(software match 'good*')" 
"problem_number|problem_synopsis|software_platform|software_version" 
[12990] search fails|embedded|2.3
[14851] generated html does not validate|server|2.1
[14928] dead links|server|2.1

=cut

