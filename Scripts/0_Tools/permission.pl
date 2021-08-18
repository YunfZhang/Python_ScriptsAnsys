#!/bin/perl
$file_name="Normal_BF01_WriteOnly.nfd";

print "\nBefore change\n--------------------\n";
system "cat $file_name";

&check_permission($file_name);

print "\nChange Permission\n--------------------\n";
system "chmod a-r $file_name";

&check_permission($file_name);

print "\nAfter change\n--------------------\n";
system "cat $file_name";

print "\nChange Permission Back\n--------------------\n";
system "chmod a+r $file_name";

&check_permission($file_name);


sub check_permission {
	my $file_name = $_[0];
	$permission=`ls -l $file_name`; 
	if ($permission=~/\s*-([-r])[-wx]{2}([-r])[-wx]{2}([-r])[-wx]{2}/) {
		($owner_read,$group_read,$other_read)=($1,$2,$3);
	} else {
		die "Error while trying to get permission of file $file_name\n";
	}
	($owner_read eq "r") ? (print "\nOwner can read\n") : (print "\nOwner cannot read\n") ;
	($group_read eq "r") ? (print "Group can read\n") : (print "Group cannot read\n");
	($other_read eq "r") ? (print "Other can read\n") : (print "Other cannot read\n");
}