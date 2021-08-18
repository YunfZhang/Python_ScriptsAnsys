#!python
import os.path
from glob import glob
import re

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2017-04-21 10:12:06 +0800 (Fri, 21 Apr 2017) $
# Revision:		$Revision: 16716 $
###############################################################################

################################################################
#The script is used to change Oid to unique in OGFX and PGFX from a file
################################################################

myStartFile = "E:/svn/SDY_r20/Test_Tracking/Tracking_Perfo/A661/Models/Main_Model/Main_Model.sgfx"
# with open(myStartFile,'r') as start_file:
	# list_Files = start_file.readlines()
	
def unique(myFile):
	myFile = re.sub(r'\n','',myFile)
	if not os.path.exists(myFile):
		print ("the file at {} is not found".format(myFile))
		quit()
	print ("start to parse the file {}".format(myFile))

	line_num = 1
	str2 = ""
	with open(myFile,'r') as file_test:
		for line in file_test:
			if re.search(r'ConnectorReference',line):
				line = re.sub(r'(.*)<intprop name="ConnectorReference">\d+', r'\1<intprop name="ConnectorReference">'+str(line_num), line)
				line_num += 1
			str2 += line
	with open(myFile,'w') as file_test:
		file_test.write(str2)
	print ("End of parsing the file: {}".format(myFile))

# for myFile in list_Files:
unique(myStartFile)


