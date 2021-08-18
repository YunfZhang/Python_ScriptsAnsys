#!python
import os.path
from glob import glob
import re

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2018-01-12 15:17:26 +0800 (周五, 12 1月 2018) $
# Revision:		$Revision: 18331 $
###############################################################################

################################################################
#The script is used to change Oid to unique in OGFX and PGFX from a folder
################################################################

start_folder = "E:/svn/Scripts/Jeff/create_models/StandardA661"
list_Files = glob("%s/*.[so]gfx" % start_folder)

def unique(myFile):
	if not os.path.exists(myFile):
		print ("the file at {} is not found".format(myFile))
		quit()
	print ("start to parse the file {}".format(myFile))

	line_num = 1
	str2 = ""
	with open(myFile,'r') as file_test:
		for line in file_test:	
			matchObj = re.match(r'.*oid=\"(\w+-\w+-\w+-\w+-\w+)\"',line)
			if matchObj: 
				str3 = matchObj.group(1)
				str3 = re.sub(r'(\w+-\w+-\w+-\w+)-\w+',r'\1-000000000000',str3)
				str3 = str3[0:len(str3)-len(str(line_num))]+str(line_num)
				line = re.sub(r'oid=\"(\w+-\w+-\w+-\w+-\w+)\"','oid=\"'+str3+'\"',line,)
				line_num += 1
			str2 += line
	with open(myFile,'w') as file_test:
		file_test.write(str2)
	print ("End of parsing the file: {}".format(myFile))

for myFile in list_Files:
	unique(myFile)


