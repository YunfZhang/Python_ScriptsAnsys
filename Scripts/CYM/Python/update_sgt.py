#!python

import sys
import os
import re
from glob import glob

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2017-11-01 17:00:17 +0800 (周三, 01 11月 2017) $
# Revision:		$Revision: 17887 $
###############################################################################


################################################################################
#the script is used to update offset value in sgt
#previous value is from 0.0~100.0
#but now, it is from 0.0~1.0
#so, all value should be divided 100.0
################################################################################

start_path = "E:\svn\SDY_r19\TCP_SDY"
# start_path = "E:\svn\SDY_r19\TCP_SDY\TCP_Simulator\Test_Data\BatchSim_Input\SDY_Objects\P_Shape\Input"

def get_files_with_extension(start_folder, extensions):
	files_list = []
	for ext in extensions:
		for d in os.walk("%s" % start_folder):
			file_ext = "*."+ext
			for f in glob(os.path.join(d[0], file_ext)):
				files_list.append("%s" % f)
	return files_list
    
suffix = ['sgt']
files = get_files_with_extension(start_path, suffix)

# print (files)


def update_sgt_offset(input):
    str1 = ""
    with open(input,'r') as f:
        for line in f:
            if "offset" in line:
                # offset_v1 = re.search(r'offset="(\d+\.\d+)"',r'\1',line)
                # offset_v2 = float(offset_v1)/100.0
                line = re.sub(r'(?<=offset=")(\d+\.\d+)', lambda m:str(float(m.group(1))/100.0), line)
            str1 += line
    with open(input, 'w') as f_out:
        f_out.write(str1)


for file in files:
    print ("\nStart to update the file: {}".format(file))
    update_sgt_offset(file)
    print ("End to update the file: {}".format(file))
    