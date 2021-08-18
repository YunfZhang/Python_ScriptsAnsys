
import os
import re
from glob import glob
import shutil


###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2017-08-29 20:12:54 +0800 (周二, 29 8月 2017) $
# Revision:		$Revision: 17452 $
###############################################################################

def get_files_with_extension(start_folder, extensions):
	files_list = []
	for ext in extensions:
		for d in os.walk("%s" % start_folder):
			file_ext = "*."+ext
			for f in glob(os.path.join(d[0], file_ext)):
				files_list.append("%s" % f)
	return files_list


if __name__ == "__main__":

	#Load Test Environment
	try: 
		import ENVIRONMENT as ENV
	except Exception as e: 
		raise Exception
		print ("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
		
	
	start_path = ENV.start_path
	SCADE_Installation_Path = ENV.SCADE_Installation_Path
	
	#update extension if you want to copy file
	#example: suffix = ['log','txt']
	suffix = ['csv']
	files = get_files_with_extension(start_path, suffix)
	
	for file in files:
		src = re.sub(r'\\','/',file)
		if re.search(r'Obtained_Results',src):
			dst = re.sub(r'Obtained_Results',r'Expected_Results',src)
			# print (src)
			# print (dst)
			dsc_directory = os.path.dirname(dst)
			if not os.path.exists(dsc_directory):
				os.makedirs(dsc_directory)
			print (dsc_directory)
			shutil.copy(src,dst)
			
	# print (files)
	
	
















