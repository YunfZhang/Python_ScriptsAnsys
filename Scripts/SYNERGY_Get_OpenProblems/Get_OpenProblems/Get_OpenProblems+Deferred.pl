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
# Last update :		$Date: 2011/05/18 03:42:02 $
# CVS version :		$Revision: 1.2 $
###############################################################################


#------------------#
## INITIALISATION ##
#------------------#
#- Variables -#
my ($read_from_file,$confID);


#-  Hash table with the information about CR/PR : %Open_Problems  -#
#------------------------------------------------------------------#
#- The scructure of the hash table %Open_Problems is as follow:
#- %Open_Problems -> '<CR-PR> Total': Total of PRs/CRs
#                    '<CR-PR> ByLevels': count of PRs/CRs in each severity level (reference to an array)
#                    '<CR-PR> Lv<showstopper>-<severe>': PRs/CRs ID of the 2 highest severity levels (reference to an array)
#                    '<CR-PR> Lv<medium-minor>': PRs/CRs ID of the lowest severity levels (reference to an array)
#
#                    '<CR-PR> List': list and details about PRs/CRs (reference to a hash table)
#                    '<CR-PR> List' -> $ID: information about the PR/CR $ID (reference to a hash table)
#                    '<CR-PR> List' -> $ID -> 'synopsis': synopsis of the PR/CR $ID
#                    '<CR-PR> List' -> $ID -> 'severity': severity level $ID
#                    '<CR-PR> List' -> $ID -> 'product': name of the product $ID
#                    '<CR-PR> List' -> $ID -> 'subprod': sub-product category $ID
# N.B: The keyword <CR-PR> has 3 values: "PR", "CR" (for CR not deferred), and "Deferred" (for CR deferred)
#      The other keywords about severity level names are processed from the configuration hash table
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
#             'CR_deferred': CR status for deferred CR (string)
#             'list_level': list of the severity levels (reference to an array)
#             'printf_info': reference to a subroutine for printing summary in the csv file Open_Problems.csv
my %Config;

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
print SYNERGY_STATUS "Database, ID, Level, Product, Status, Synopsis\n\n";


#- Add 3 keys for problem severity to %Config: showstopper, severe, medium-minor-#
$Config{'showstopper'}=$Config{'list_level'}->[0];
$Config{'severe'}=$Config{'list_level'}->[1];
$Config{'medium_minor'}="$Config{'list_level'}->[2]-".$Config{'list_level'}->[@{$Config{'list_level'}}-1];

foreach my $CRPR ("PR","CR") {

	#- Add 2 keys depending if it is a CR or a PR: database and no_status -#
	$Config{'database'} = ( ($CRPR eq "PR") ? $Config{'database_PR'} : $Config{'database_CR'} );
	$Config{'no_status'} = ( ($CRPR eq "PR") ? $Config{'no_status_PR'} : $Config{'no_status_CR'} );

	#---------------------------#
	## 		Retrieve CR/PR	   ##
	#---------------------------#
	print "\n$CRPR List\n","-"x 20,"\n";

	$read_from_file or &print_list_FromSynergy(\%Config);
	my %h_listCRPR=&getProblems_FromFile($CRPR,$Config{'csv_PbList'});

	# #- Get the information for the CRs/PRs -#
	&process_PRCR($CRPR, \%Config, \%Open_Problems);

	#- Summarize the information -#
	for (my $i=0;$i<@{$Config{'list_level'}};$i++) {
		print "Level $Config{'list_level'}->[$i]: $Open_Problems{\"$CRPR ByLevels\"}->[$i]\n"; 
	}
	print "=>TOTAL = $Open_Problems{\"$CRPR Total\"} $CRPR\n";

	#- Print information about Showstoppers -#
	my @list_showstoppers= grep { $Config{'showstopper'}=~/$Open_Problems{"$CRPR List"}->{$_}->{'level'}/ } (sort keys %{$Open_Problems{"$CRPR List"}});
	if (scalar @list_showstoppers) {
		print "-"x 20,"\n--$CRPR level $Config{'showstopper'}--\n";
		map { printf "*$CRPR-%d: %s\n", $_, $Open_Problems{"$CRPR List"}->{$_}->{'synopsis'} } (@list_showstoppers);
	} else {}
	print "-"x 32,"\n\n";


}
#- Close the file with results from SYNERGY -#
close SYNERGY_STATUS;

# #- Get the information for the deferred CR -#
&process_PRCR("Deferred", \%Config, \%Open_Problems);

#- Print the summary in a file -#
&print_summary($Config{'list_level'}, $Config{'printf_info'}, \%Open_Problems);


#------------------#
##      END       ##
#------------------#



#-- Subroutine "process_PRCR" --#
#-------------------------------#
#-- process a PR/CR by doing: --#
#--   * read information from the file
#--   * count the PR/RCs in each level
#--   * count the total of PR/CRs 
#---------- INPUT ----------# 
#  1. $CRPR -> type of PR/CR ("PR", "CR", or "Deferred")
#  2. $rh_Config -> reference to the hash table with the configuration
#  3. $rh_Open_Pb -> reference to the hash table with the Open Problems
 sub process_PRCR {
	my ($CRPR, $rh_Config, $rh_Open_Pb) =@_;

	#- Read the information from the file -#
	%{$rh_Open_Pb->{"$CRPR List"}}=&getProblems_FromFile($CRPR,$rh_Config->{'csv_PbList'});

	#- Calculate the total of PRs/CRs and the number in each level -#
	$rh_Open_Pb->{"$CRPR Total"}=&count_level($CRPR, $rh_Open_Pb, $rh_Config->{'list_level'});

	#- List showstopper and severe PRs/CRs -#
	my %showstopper=&get_level($rh_Open_Pb->{"$CRPR List"},$rh_Config->{'showstopper'});
	my %severe=&get_level($rh_Open_Pb->{"$CRPR List"},$rh_Config->{'severe'});
	@{$rh_Open_Pb->{"$CRPR Lv$rh_Config->{'showstopper'}-$rh_Config->{'severe'}"}} = ( keys %showstopper, keys %severe );
 
	#- List medium and minor PRs/CRs -#
	foreach my $level (@{$rh_Config->{'list_level'}}[2..@{$rh_Config->{'list_level'}}-1]) {
		my %list_pb=&get_level($rh_Open_Pb->{"$CRPR List"},$level);
		push( @{$rh_Open_Pb->{"$CRPR Lv$rh_Config->{'medium_minor'}"}} , keys %list_pb );
	}
 
 }


#------------------------------------------------------------------------------------------------------------------------------------------#
##                              -----------------    SUBROUTINE   -----------------------------                                           ##
#------------------------------------------------------------------------------------------------------------------------------------------#


#-- Subroutine "print_list_FromSynergy" --#
#-----------------------------------------#
#-- process queries from Synergy to print a list --#
#---------- INPUT ----------# 
#  1. $rh_Config -> reference to the hash table with the configuration
sub print_list_FromSynergy {
	my $rh_Config = shift;

	#- Process argument : $ra_no_status -#
	my @no_status=@{$rh_Config->{'no_status'}};
	map { s/^'?(\w.*\w)'?$/'$1'/ } @no_status;

	#- Print Headers -#
	print "Database $Config{'database'}\n";

	#- Query of Synergy -#
	my $query="(cvtype='problem')"; #- Initiate the query -#
	$query.=" and ("; $query.=join(" or ",map { "(severity='$_')"} @{$rh_Config->{'list_level'}} );$query.=")"; #- Add the levels -#
	map { $query.=" and (crstatus!=$_) " } @no_status; #- Add the exception on the status -#
	if ($rh_Config->{'prod_query'}) { $query.=" and ($rh_Config->{'prod_query'})"; } #if we have added a query on the products and category
	# print "QUERY = $query\n"; #FOR DEBUG#

	#- Format, depending on whether it is a CR or a PR, and FIELDS -#
	my $CRPR= ($rh_Config->{'database'}=~/^PR/) ? "PR" : "CR";
	my $format= "$CRPR-%d,%s,%s,%s,%s,\"%s\"";
	my $fields=" problem_number severity product_name product_subsys crstatus problem_synopsis";

	#- Result of the Synergy Request -#
	my $SYN_result=`perl getreport.pl -f "$format" -q "$query" -d "$rh_Config->{'database'}" $fields`;
	my @list_Pb=split(/\n/,$SYN_result); 
	@list_Pb=map {"$rh_Config->{'database'},$_"} @list_Pb;

	#- Print the report in CSV file -#
	map { print SYNERGY_STATUS "$_\n" } @list_Pb;
	print SYNERGY_STATUS "\n";
	
	#- End -#
	print "Results for $rh_Config->{'database'} printed\n";
	return;
}


#-- Subroutine "getProblems_FromFile" --#
#---------------------------------------#
#-- process data printed out by print_list_FromSynergy --#
sub getProblems_FromFile {
	#---------- INPUT ----------# 
	#  1. $CRPR -> To indicate if we deal with CR or PR
	my ($CRPR, $csv_PbList)=@_;
	#---------- OUTPUT ----------# 
	#  %h_listProblems : hash table with the information from SYNERGY. 
	#              The hash table is a succession of hash tables whose values are pointers to other hash tables; it is as follow:
	#	%h_listProblems -> CR/PR id -> 'synopsis': synopsis of the PR/CR
	#                               -> 'severity': severity level
	#                               -> 'product': name of the product
	#                               -> 'subprod': sub-product category
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
			if ( (($CRPR eq "Deferred") && ($status=~/deferred/)) or 
			     (($CRPR ne "Deferred") && ($prefix eq $CRPR) && ($status!~/deferred/)) )
			{
				$h_listProblems{$id}->{'synopsis'}=$synopsis;
				$h_listProblems{$id}->{'level'}=$level;
				$h_listProblems{$id}->{'status'}=$status;
				$h_listProblems{$id}->{'product'}=$product;
				$h_listProblems{$id}->{'subprod'}=$subprod;
			} else {}
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
#------------------------------#
#-- count the number of problems for each level of severity --#
sub count_level {
	#---------- INPUT ----------# 
	#  1. $CRPR -> To indicate if we deal with a PR, a CR, or a deferred CR
	#  2. $rh_Open_Pb -> pointer to the hash table with all the open problems
	#  3. $ra_list_level -> pointer to the list of severity levels for the problems we want
	my ($CRPR, $rh_Open_Pb, $ra_list_level)=@_;
	#---------- OUTPUT ----------# 

	#- Number of problems in each level -#
	foreach my $level (@$ra_list_level) {
		my $count_level=0;
		foreach (keys %{$rh_Open_Pb->{"$CRPR List"}}) {
			$count_level += ($rh_Open_Pb->{"$CRPR List"}->{$_}->{'level'}=~/$level/);
		}
		push(@{$rh_Open_Pb->{"$CRPR ByLevels"}}, $count_level);
	}

	#  Calculate $total_pb : total number of problems for all levels
	my $total_pb=0;
	map { $total_pb+=$_ } @{$rh_Open_Pb->{"$CRPR ByLevels"}};

	return $total_pb;
}



#-- Subroutine "get_level" --#
#----------------------------#
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
#--------------------------------#
#-- print the summary of CR/PR in a csv file --#
sub print_summary { 
	my ($ra_level,$rs_printf_info,$rh_Open_Pb) = @_;
	my @list_level=@$ra_level;

	open OPEN_PROBLEMS, ">Open_Problems.csv" or die $!;

	#- Print the number of CR/PR for each level of severity -#
	print OPEN_PROBLEMS   ", ",join(", ", @list_level),", TOTAL\n";
	print OPEN_PROBLEMS "PR, ",join(", ", @{$rh_Open_Pb->{"PR ByLevels"}})," , ",$rh_Open_Pb->{"PR Total"},",\n";
	print OPEN_PROBLEMS "CR, ",join(", ", @{$rh_Open_Pb->{"CR ByLevels"}})," , ",$rh_Open_Pb->{"CR Total"},",\n";
	print OPEN_PROBLEMS "CR deferred, ",join(", ", @{$rh_Open_Pb->{"Deferred ByLevels"}})," , ",$rh_Open_Pb->{"Deferred Total"},",\n";
	print OPEN_PROBLEMS "\n";
	
	#- Print the list of CR/PR for each group of severity -#
	foreach my $level ("$Config{'showstopper'}-$Config{'severe'}","$Config{'medium_minor'}") {
		# foreach my $CRPR ("PR", "CR") {
		foreach my $CRPR ("PR", "CR", "Deferred") {
			print OPEN_PROBLEMS "List of level $level opened ",(($CRPR eq "Deferred") ? "CR deferred:\n" : "${CRPR}s:\n");
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
		$Config{'SDYIDE'}->{'prod_query'}="((product_name='DISPLAY-IDE') or (product_name='SUITE-IDE' and (product_subsys='Rapid Prototyper' or product_subsys='Display integration')) or (product_name='SCADE LifeCycle' and (product_subsys='RM Gateway' or product_subsys='RM Display Coupling') or product_subsys='Reporter Common' or product_subsys='Reporter Display' or product_subsys='User Documentation'))";
		$Config{'SDYIDE'}->{'database_PR'}="PR_ET_SCADE";
		$Config{'SDYIDE'}->{'database_CR'}="CR_SCADE";
		@{$Config{'SDYIDE'}->{'no_status_PR'}} =("PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation","PR_closed_by_CR");
		@{$Config{'SDYIDE'}->{'no_status_CR'}} =("CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");
		$Config{'SDYIDE'}->{'deferred_CR'}="CR_deferred";

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
		@{$Config{'SDYKCG'}->{'no_status_PR'}} =("KCG_concluded","KCG_rejected","KCG_duplicate","KCG_tested","KCG_obsolete","KCG_migrated","KCG_closed_by_CR_creation");
		@{$Config{'SDYKCG'}->{'no_status_CR'}} =("CR_KCG_concluded","CR_KCG_rejected","CR_KCG_duplicate","CR_KCG_tested","CR_KCG_obsolete","CR_KCG_migrated");
		$Config{'SDYKCG'}->{'deferred_CR'}="CR_KCG_deferred";

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
		@{$Config{'OGLX'}->{'no_status_PR'}} =("KCG_concluded","KCG_rejected","KCG_duplicate","KCG_tested","KCG_obsolete","KCG_migrated","KCG_closed_by_CR_creation");
		@{$Config{'OGLX'}->{'no_status_CR'}} =("CR_KCG_concluded","CR_KCG_rejected","CR_KCG_duplicate","CR_KCG_tested","CR_KCG_obsolete","CR_KCG_migrated");
		$Config{'OGLX'}->{'deferred_CR'}="CR_KCG_deferred";
		
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
		@{$Config{'SCIDE'}->{'no_status_PR'}} =("PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation");
		@{$Config{'SCIDE'}->{'no_status_CR'}} =("CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");
		$Config{'SCIDE'}->{'deferred_CR'}="CR_deferred";

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
		$Config{'A661'}->{'prod_query'}="((product_name='SCADE A661'))";
		$Config{'A661'}->{'database_PR'}="PR_ET_SCADE";
		$Config{'A661'}->{'database_CR'}="CR_SCADE";
		@{$Config{'A661'}->{'no_status_PR'}} =("PR_concluded","PR_rejected","PR_duplicate","PR_tested","PR_obsolete","PR_migrated","PR_for_CR_creation","PR_closed_by_CR");
		@{$Config{'A661'}->{'no_status_CR'}} =("CR_concluded","CR_rejected","CR_duplicate","CR_tested","CR_obsolete","CR_migrated");
		$Config{'A661'}->{'deferred_CR'}="CR_deferred";

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

