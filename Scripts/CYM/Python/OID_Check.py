#!python
import os.path
from glob import glob
import re

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date:				$Date: 2018-06-25 17:03:48 +0800 (周一, 25 6月 2018) $
# Revision:			$Revision: 19703 $
###############################################################################


################################################################
#The script is used to check Oid is duplicated in OGFX and PGFX?
################################################################


start_folder = "E:/svn/SDY_IDE1/Scripts/CYM/Python/SteamBoiler"
list_Files = glob("%s/*.[so]gfx" % start_folder)

# print list_Files

def GetDuplicateOID(myFile):
	if not os.path.exists(myFile):
		print ("the file at {} is not found".format(myFile))
		quit()
	print ("start to parse the file {}".format(myFile))
	list1 = []
	list_Dup = []
	line_num = 1
	with open("a.log", 'a') as logtowrite:
		logtowrite.write(myFile)
		logtowrite.write("\n")
	with open(myFile,'r') as file_test:
		for line in file_test:
			line_num += 1
			matchObj = re.match(r'.*oid=\"(\w+-\w+-\w+-\w+-\w+)\"',line)
			if matchObj: 
				str1 = matchObj.group(1)
				if str1 in list1:
					with open("a.log", 'a') as logtowrite2:
						logtowrite2.write(str(line_num))
						logtowrite2.write("    ")
						logtowrite2.write(str(str1))
						logtowrite2.write("\n")
					list_Dup.append(line_num)
				else:
					list1.append(str1)
	# print "start to print oid for file: {}".format(myFile)
	# print list1
	# print "End of print file: {}".format(myFile)
	# return list_Dup

# myFile = "C:/svnfiles/SDY_A661_R19/Test_Tracking/Tracking_Perfo/Models/Main_Model/Main_Model.sgfx"	
# duplicated_lines = GetDuplicateOID(myFile)
# print duplicated_lines
# quit()
for myFile in list_Files:
	GetDuplicateOID(myFile)