#!perl
$|=1;
use strict;

# Get_Open_Problems --
#
#  Scripts to retrieve information  from SYNERGY and print a summary in a CSV file 
#
# Copyright (c) 2010 Esterel-Technologies
#
###################### Configuration management information : ################# 
# Creator     :		Jean-Francois Thuong
# Last updater:		$Author: chenym $
# Last update :		$Date: 2011/03/02 07:02:23 $
# CVS version :		$Revision: 1.2 $
###############################################################################


#------------------#
## INITIALISATION ##
#------------------#
#- Variables -#
my ($read_from_file,$confID);
my %Open_Problems; #global report of Open_Problems

#-  Hash table for the configuration of the different products    -#
#-   N.B: the different configurations are at the end of the file -#
#------------------------------------------------------------------#
#- The scructure of the hash table %Config is as follow:
#- %Config -> 'csv_PbList': file in which to save the result of the SYNERGY query
#             'prod_query': optional query on the products and sub-products
#             'database_PR': name of the database for the PR
#             'database_CR': name of the database for the CR
#             'no_status_PR': list of the status that shall be skipped for PR (reference to an array)
#             'no_status_CR': list of the status that shall be skipped for CR (reference to an array)
#             'list_level': list of the severity levels (reference to an array)
#             'printf_info': reference to a subroutine for printing summary in the csv file Open_Problems.csv
our %Config;

#- Choice from the user to read from SYNERGY or from a file ($csv_PbList) -#
print "----------\nRead information from SYNERGY ( [Yy]es=Default, [Nn]o )?  ";
my $answer_read = <STDIN>;
if ($answer_read =~ /^\s*$/ or $answer_read =~ /^y(es)?/i) {
	$read_from_file=0;
} elsif ($answer_read =~ /^no?/i) {
	$read_from_file=1;
} else {
	print "WARNING: answer is neither \"yes\" or \"no\": the answer \"yes\" is used as default\n";
	$read_from_file=0;
}


#- Choice of the user for the configuration -#
print "----------\nWhich configuration do you want ( 1=SDYIDE | 2=SDYKCG | 3=OGLX | 4=SCIDE | 5=A661 )?  ";
my $answer_config = <STDIN>;
if ($answer_config =~ /^1\s*$/ or $answer_config =~ /^SDYIDE/i) {
	%Config=&get_config('SDYIDE');
} elsif ($answer_config =~ /^2\s*$/ or $answer_config =~ /^SDYKCG/i) {
	%Config=&get_config('SDYKCG');
} elsif ($answer_config =~ /^3\s*$/ or $answer_config =~ /^OGLX/i) {
	%Config=&get_config('OGLX');
} elsif ($answer_config =~ /^4\s*$/ or $answer_config =~ /^SCIDE/i) {
	%Config=&get_config('SCIDE');
} elsif ($answer_config =~ /^5\s*$/ or $answer_config =~ /^A661/i) {
	%Config=&get_config('A661');
} else {
	%Config=();
}


#---------------------------#
## PROCESS THE INFORMATION ##
#---------------------------#
$read_from_file or open SYNERGY_STATUS, ">$Config{csv_PbList}" or die "Error while trying to open $Config{csv_PbList}: $!";
print SYNERGY_STATUS "Database, ID, Level, Product, Moduloe, Status, Synopsis\n\n";


#- Set the 3 categories of problem severity -#
my @list_level=@{$Config{'list_level'}};
my $showstopper=$list_level[0];
my $severe=$list_level[1];
my $medium_minor="$list_level[2]-".$list_level[@list_level-1];

foreach my $CRPR ("PR","CR") {

	#- Find the data for the query -#
	my $database=( ($CRPR eq "PR") ? $Config{'database_PR'} : $Config{'database_CR'} );
	my @no_status = ( ($CRPR eq "PR") ? @{$Config{'no_status_PR'}} : @{$Config{'no_status_CR'}} );
	
	#---------------------------#
	## 		Retrieve CR/PR	   ##
	#---------------------------#
	print "\n$CRPR List\n","-"x 20,"\n";

	$read_from_file or &print_list_FromSynergy($database,\@list_level,\@no_status, $Config{'prod_query'});
	my %h_listCRPR=&getProblems_FromFile($CRPR,$Config{csv_PbList});
	
	#- Print the number of problems in each level -#
	my @count;
	my $total=&count_level(\%h_listCRPR,\@list_level,\@count);
	for (my $i=0;$i<@list_level;$i++) {
		print "Level $list_level[$i]: $count[$i]\n"; 
	}
	print "=>TOTAL = $total $CRPR\n";

	#- Print the problems of highest level -#
	my %showstopper=&get_level(\%h_listCRPR,$showstopper);
	unless (scalar keys %showstopper == 0) {
		print "-"x 20,"\n--$CRPR level $showstopper--\n";
		map { printf "*$CRPR-%d: %s\n",$_,$showstopper{$_}; } (sort keys %showstopper);
	}
	print "-"x 32,"\n\n";

	#- Summarize the information -#
	my %severe=&get_level(\%h_listCRPR,$severe);
	%{$Open_Problems{"$CRPR List"}}=%h_listCRPR; #Hash with the list and details about CR/PR
	$Open_Problems{"$CRPR Total"} = $total;
	@{$Open_Problems{"$CRPR ByLevels"}} = @count;
	@{$Open_Problems{"$CRPR Lv$showstopper-$severe"}} = ( keys %showstopper, keys %severe );
	foreach my $level (@list_level[2..@list_level-1]) {
		my %list_pb=&get_level(\%h_listCRPR,$level);
		push( @{$Open_Problems{"$CRPR Lv$medium_minor"}} , keys %list_pb );
	}
}
#- Close the file with results from SYNERGY -#
close SYNERGY_STATUS;

#- Print the summary in a file -#
&print_summary(\@list_level, $Config{'printf_info'},%Open_Problems);


#------------------#
##      END       ##
#------------------#
 


#------------------------------------------------------------------------------------------------------------------------------------------#
##                              -----------------    SUBROUTINE   -----------------------------                                           ##
#------------------------------------------------------------------------------------------------------------------------------------------#


#-- Subroutine "print_list_FromSynergy" --#
#-- process queries from Synergy to print a list --#
sub print_list_FromSynergy {
	#---------- INPUT ----------# 
	#  1. $database -> string with the name of the database
	#  2. $ra_list_level -> pointer to the list of severity levels for the problems we want
	#  3. $ra_no_status -> pointer to the list of status that shall be skipped in the list of CR/PR
	my ($database,$ra_list_level,$ra_no_status, $prod_query)=@_;
	
	#- Process argument : $ra_no_status -#
	my @no_status=@$ra_no_status;
	map { s/^'?(\w.*\w)'?$/'$1'/ } @no_status;
	
	#- Print Headers -#
	print "Database $database\n";
	
	#- Query of Synergy -#
	my $query="(cvtype='problem')"; #- Initiate the query -#
	$query.=" and ("; $query.=join(" or ",map { "(severity='$_')"} @$ra_list_level );$query.=")"; #- Add the levels -#
	map { $query.=" and (crstatus!=$_) " } @no_status; #- Add the exception on the status -#
	if ($prod_query) { $query.=" and ($prod_query)"; } #if we have added a query on the products and category
	# print "QUERY = $query\n"; #FOR DEBUG#

	#- Format, depending on whether it is a CR or a PR, and FIELDS -#
	my $PRCR= ($database=~/^PR/) ? "PR" : "CR";
	my $format= "$PRCR-%d,%s,%s,%s,%s,\"%s\"";
	my $fields=" problem_number severity product_name product_subsys crstatus problem_synopsis";

	#- Result of the Synergy Request -#
	my $SYN_result=`perl getreport.pl -f "$format" -q "$query" -d "$database" $fields`;
	my @list_Pb=split(/\n/,$SYN_result); 
	@list_Pb=map {"$database,$_"} @list_Pb;

	#- Print the report in CSV file -#
	map { print SYNERGY_STATUS "$_\n" } @list_Pb;
	print SYNERGY_STATUS "\n";
	
	#- End -#
	print "Results for $database printed\n";
	return;
}


#-- Subroutine "getProblems_FromFile" --#
#-- process data printed out by print_list_FromSynergy --#
sub getProblems_FromFile {
	#---------- INPUT ----------# 
	#  1. $PRCR -> To indicate if we deal with CR or PR
	my ($PRCR, $csv_PbList)=@_;
	#---------- OUTPUT ----------# 
	#  %h_listProblems : hash table with the information from SYNERGY. 
	#              The hash table is a succession of hash tables whose values are pointers to other hash tables; it is as follow:
	#	%h_listProblems -> CR/PR id -> 'synopsis': synopsis of the PR/CR (a string)
	#                               -> 'severity': severity level
	#                               -> 'product': name of the product (a string)
	#                               -> 'subprod': sub-product category (a string)
	#                               -> 'status': CR/PR status
	# e.g. $h_listProblems -> {'492'} -> {'synopsis'} = "OGLX: The first parameter is wrong for glStencilFunc..."
	# e.g. $h_listProblems -> {'492'} -> {'level'} = "1"
	# e.g. $h_listProblems -> {'492'} -> {'product'} = 'OGLX'
	my %h_listProblems=();

	#- Read the data (report) from the CSV file -#
	my $SYN_result=`cat $csv_PbList`;
	my @list_Pb=split(/\n/,$SYN_result);

	#- Save the data in the hash table -#
	foreach (@list_Pb) {
		if (/^\w+,([PC]R)-(\d+),(\w+),([^,]+),([^,]+),(\w+),(.*)$/) {
			my ($prefix,$id,$level,$product,$subprod,$status,$synopsis)=($1,$2,$3,$4,$5,$6,$7);
			if ($prefix eq $PRCR) {
				$h_listProblems{$id}->{'synopsis'}=$synopsis;
				$h_listProblems{$id}->{'level'}=$level;
				$h_listProblems{$id}->{'status'}=$status;
				$h_listProblems{$id}->{'product'}=$product;
				$h_listProblems{$id}->{'subprod'}=$subprod;
			}
		} elsif (/^(Database.*|\s*)$/) {
			#Skip lines for header or empty lines
		} else {
			print "Wrong pattern in: $_\n";
		}
	}
	
	#- Return the output (hash table) -#
	return %h_listProblems;
}


#-- Subroutine "count_level" --#
#-- count the number of problems for each level of severity --#
sub count_level {
	#---------- INPUT ----------# 
	#  1. $rh_synergy -> pointer to the hash table returned by the subroutine getProblems_FromFile
	#  2. $ra_list_level -> pointer to the list of severity levels for the problems we want
	#  3. $ra_count_level -> pointer to the number of problems in each severity level (processed by the subroutine)
	my ($rh_synergy,$ra_list_level,$ra_count_level)=@_;
	#---------- OUTPUT ----------# 
	#  $total_pb : total number of problems within the given severity levels in argument 
	my $total_pb=0;
	
	
		#- Number of problems in each level -#
	my @count;
	foreach my $level (@$ra_list_level) {
		my $count_level=0;
		map { $count_level += ($rh_synergy->{$_}->{'level'}=~/$level/) } keys %{$rh_synergy};
		push(@count, $count_level);
	}
	
		#- Calculate the sum -#
	map { $total_pb+=$_ } @count;
	
	@{$ra_count_level}=@count;
	return $total_pb;
}



#-- Subroutine "get_level" --#
#-- get the CR/PR of a given level --#
sub get_level {
	#---------- INPUT ----------# 
	#  1. $rh_synergy -> pointer to the hash table returned by the subroutine getProblems_FromFile
	#  2. $level -> the severity level from which we want the CR/PR
	my ($rh_synergy,$level)=@_;
	#---------- OUTPUT ----------# 
	#  %list_level : hash table whose keys are the PR/CR id and the value is the synopsis
	my %list_level;
	foreach (keys %{$rh_synergy}) {
		if ( $rh_synergy->{$_}->{'level'}=~/$level/) {
			$list_level{$_}=$rh_synergy->{$_}->{'synopsis'};
		}
	}
	
	return %list_level;
}


#-- Subroutine "print_summary" --#
#-- print the summary of CR/PR in a csv file --#
sub print_summary { 
	my ($ra_level,$rs_printf_info,%Open_Problems) = @_;
	my @list_level=@$ra_level;

	open OPEN_PROBLEMS, ">Open_Problems.csv" or die $!;

	print OPEN_PROBLEMS   ", ",join(", ", @list_level),", TOTAL\n";
	print OPEN_PROBLEMS "PR, ",join(", ", @{$Open_Problems{"PR ByLevels"}})," , ",$Open_Problems{"PR Total"},",\n";
	print OPEN_PROBLEMS "CR, ",join(", ", @{$Open_Problems{"CR ByLevels"}})," , ",$Open_Problems{"CR Total"},",\n";
	print OPEN_PROBLEMS "\n";
	
	foreach my $level ("$showstopper-$severe","$medium_minor") {
		foreach my $CRPR ("PR", "CR") {
			print OPEN_PROBLEMS "List of level $level opened ${CRPR}s:\n";
			&$rs_printf_info($CRPR, $level, %Open_Problems);
			print OPEN_PROBLEMS "\n";
		}
		print OPEN_PROBLEMS "\n";
	}
	
	print OPEN_PROBLEMS "\n";

	close OPEN_PROBLEMS or die $!;
}



#------------------------------------------------------------------------------------------------------------------------------------------#
##                              -----------------    CONFIGURATION   -----------------------------                                           ##
#------------------------------------------------------------------------------------------------------------------------------------------#


sub get_config{
	my $confID=$_[0];
	my %Config;
	
	#-----------------------------#
	## CONFIGURATION FOR SDY IDE ##
	#-----------------------------#
	SDYIDE: {
		$Config{'SDYIDE'}->{'csv_PbList'}="CRPR_status_IDE.csv";
		
		#- Configuration for SYNERGY queries -#
		$Config{'SDYIDE'}->{'prod_query'}="(product_name='DISPLAY-IDE') or (product_name='SUITE-IDE' and (product_subsys='Display integration')) or (product_name='SCADE LifeCycle' and (product_subsys='RM Gateway' or product_subsys='RM Display Coupling') or product_subsys='Reporter Common' or product_subsys='Reporter Display' or product_subsys='User Documentation')";
		$Config{'SDYIDE'}->{'database_PR'}="PR_ET_SCADE";
		$Config{'SDYIDE'}->{'database_CR'}="CR_SCADE";
		@{$Config{'SDYIDE'}->{'no_status_PR'}} =("PR_deferred","PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation","PR_closed_by_CR");
		@{$Config{'SDYIDE'}->{'no_status_CR'}} =("CR_deferred","CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");

		#- Set the levels of severity -#
		@{$Config{'SDYIDE'}->{'list_level'}}=("Showstopper","Severe","Medium", "Minor");

		#- Subroutine to print information in Open_Problems.csv -#
		$Config{'SDYIDE'}->{'printf_info'} = sub {
			my ($CRPR, $level, %Open_Problems) = @_;
			my $n_pb=1;
			printf OPEN_PROBLEMS "%2s, %4s,%-21s,\"%s\", %8s, %s\n", 'No', "${CRPR}ID", '"Category"', 'Synopsis', 'Severity', 'Status'; 
			foreach my $ID ( sort @{$Open_Problems{"$CRPR Lv$level"}} ) {
				my %info=%{$Open_Problems{"$CRPR List"}->{$ID}};
				printf OPEN_PROBLEMS "%2d, %4s,%-21s,\"%s\", %8s, %s\n", $n_pb++, $ID, "\"".$info{'subprod'}."\"", $info{'synopsis'}, $info{'level'}, $info{'status'}; 
			}
			return;
		};
	}

	#-----------------------------#
	## CONFIGURATION FOR SDY KCG ##
	#-----------------------------#
	SDYKCG: {
		$Config{'SDYKCG'}->{'csv_PbList'}="CRPR_status.csv";
		
		#- Configuration for SYNERGY queries -#
		$Config{'SDYKCG'}->{'prod_query'}="product_name='SDYKCG'";
		$Config{'SDYKCG'}->{'database_PR'}="PR_DISPLAY_KCG";
		$Config{'SDYKCG'}->{'database_CR'}="CR_DISPLAY_KCG";
		@{$Config{'SDYKCG'}->{'no_status_PR'}} =("KCG_deferred","KCG_concluded","KCG_rejected","KCG_duplicate","KCG_tested","KCG_obsolete","KCG_migrated","KCG_closed_by_CR_creation");
		@{$Config{'SDYKCG'}->{'no_status_CR'}} =("CR_KCG_deferred","CR_KCG_concluded","CR_KCG_rejected","CR_KCG_duplicate","CR_KCG_tested","CR_KCG_obsolete","CR_KCG_migrated");

		#- Set the levels of severity -#
		@{$Config{'SDYKCG'}->{'list_level'}}=(1..6);

		#- Subroutine to print information in Open_Problems.csv -#
		$Config{'SDYKCG'}->{'printf_info'} = sub {
			my ($CRPR, $level, %Open_Problems) = @_;
			my $n_pb=1;
			printf OPEN_PROBLEMS "%2s, %4s, %8s,\"%s\", %s\n", 'No', "${CRPR}ID",'Severity', 'Synopsis', 'Status'; 
			foreach my $ID ( sort @{$Open_Problems{"$CRPR Lv$level"}} ) {
				my %info=%{$Open_Problems{"$CRPR List"}->{$ID}};
				printf OPEN_PROBLEMS "%2d, %4s, %8s,\"%s\", %s\n", $n_pb++, $ID, $info{'level'}, $info{'synopsis'}, $info{'status'}; 
			}
			return;
		};
	}

	#--------------------------#
	## CONFIGURATION FOR OGLX ##
	#--------------------------#
	OGLX: {
		$Config{'OGLX'}->{'csv_PbList'}="CRPR_status.csv";
		
		#- Configuration for SYNERGY queries -#
		$Config{'OGLX'}->{'prod_query'}="product_name='OGLX'";
		$Config{'OGLX'}->{'database_PR'}="PR_DISPLAY_KCG";
		$Config{'OGLX'}->{'database_CR'}="CR_DISPLAY_KCG";
		@{$Config{'OGLX'}->{'no_status_PR'}} =("KCG_deferred","KCG_concluded","KCG_rejected","KCG_duplicate","KCG_tested","KCG_obsolete","KCG_migrated","KCG_closed_by_CR_creation");
		@{$Config{'OGLX'}->{'no_status_CR'}} =("CR_KCG_deferred","CR_KCG_concluded","CR_KCG_rejected","CR_KCG_duplicate","CR_KCG_tested","CR_KCG_obsolete","CR_KCG_migrated");

		#- Set the levels of severity -#
		@{$Config{'OGLX'}->{'list_level'}}=(1..5);

		#- Subroutine to print information in Open_Problems.csv -#
		$Config{'OGLX'}->{'printf_info'} = sub {
			my ($CRPR, $level, %Open_Problems) = @_;
			my $n_pb=1;
			printf OPEN_PROBLEMS "%2s, %4s, %8s,\"%s\", %s\n", 'No', "${CRPR}ID",'Severity', 'Synopsis', 'Status'; 
			foreach my $ID ( sort @{$Open_Problems{"$CRPR Lv$level"}} ) {
				my %info=%{$Open_Problems{"$CRPR List"}->{$ID}};
				printf OPEN_PROBLEMS "%2d, %4s, %8s,\"%s\", %s\n", $n_pb++, $ID, $info{'level'}, $info{'synopsis'}, $info{'status'}; 
			}
			return;
		};
	}

	#-------------------------------#
	## CONFIGURATION FOR SUITE IDE ##
	#-------------------------------#
	SCIDE: {
		$Config{'SCIDE'}->{'csv_PbList'}="CRPR_status_IDE.csv";
		
		#- Configuration for SYNERGY queries -#
		$Config{'SCIDE'}->{'prod_query'}="(product_name='SUITE-IDE') or (product_name='SCADE RM Gateway') or (product_name='ET-SCADE')";
		$Config{'SCIDE'}->{'database_PR'}="PR_ET_SCADE";
		$Config{'SCIDE'}->{'database_CR'}="CR_SCADE";
		@{$Config{'SCIDE'}->{'no_status_PR'}} =("PR_deferred","PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation");
		@{$Config{'SCIDE'}->{'no_status_CR'}} =("CR_deferred","CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");

		#- Set the levels of severity -#
		@{$Config{'SCIDE'}->{'list_level'}}=("Showstopper","Severe","Medium", "Minor");

		#- Subroutine to print information in Open_Problems.csv -#
		$Config{'SCIDE'}->{'printf_info'} = sub {
			my ($CRPR, $level, %Open_Problems) = @_;
			my $n_pb=1;
			printf OPEN_PROBLEMS "%2s, %4s,%-21s,\"%s\", %8s, %s\n", 'No', "${CRPR}ID", '"Category"', 'Synopsis', 'Severity', 'Status'; 
			foreach my $ID ( sort @{$Open_Problems{"$CRPR Lv$level"}} ) {
				my %info=%{$Open_Problems{"$CRPR List"}->{$ID}};
				printf OPEN_PROBLEMS "%2d, %4s,%-21s,\"%s\", %8s, %s\n", $n_pb++, $ID, "\"".$info{'subprod'}."\"", $info{'synopsis'}, $info{'level'}, $info{'status'}; 
			}
			return;
		};
	}
	
	#-----------------------------#
	## CONFIGURATION FOR ARINC 661 ##
	#-----------------------------#
	A661: {
		$Config{'A661'}->{'csv_PbList'}="CRPR_status_A661.csv";
		
		#- Configuration for SYNERGY queries -#
		$Config{'A661'}->{'prod_query'}="(product_name='SCADE A661')";
		$Config{'A661'}->{'database_PR'}="PR_ET_SCADE";
		$Config{'A661'}->{'database_CR'}="CR_SCADE";
		@{$Config{'A661'}->{'no_status_PR'}} =("PR_deferred","PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation","PR_closed_by_CR");
		@{$Config{'A661'}->{'no_status_CR'}} =("CR_deferred","CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");

		#- Set the levels of severity -#
		@{$Config{'A661'}->{'list_level'}}=("Showstopper","Severe","Medium", "Minor");

		#- Subroutine to print information in Open_Problems.csv -#
		$Config{'A661'}->{'printf_info'} = sub {
			my ($CRPR, $level, %Open_Problems) = @_;
			my $n_pb=1;
			printf OPEN_PROBLEMS "%2s, %4s,%-21s,\"%s\", %8s, %s\n", 'No', "${CRPR}ID", '"Category"', 'Synopsis', 'Severity', 'Status'; 
			foreach my $ID ( sort @{$Open_Problems{"$CRPR Lv$level"}} ) {
				my %info=%{$Open_Problems{"$CRPR List"}->{$ID}};
				printf OPEN_PROBLEMS "%2d, %4s,%-21s,\"%s\", %8s, %s\n", $n_pb++, $ID, "\"".$info{'subprod'}."\"", $info{'synopsis'}, $info{'level'}, $info{'status'}; 
			}
			return;
		};
	}


	#-----------------#
	## END OF CONFIG ##
	#-----------------#
	print "CONFIG = $confID\n";
	return %{$Config{$confID}};
}

