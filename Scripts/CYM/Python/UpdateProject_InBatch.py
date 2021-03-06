import os
import sys
import re
from glob import glob  

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2017-09-06 09:44:00 +0800 (周三, 06 9月 2017) $
# Revision:		$Revision: 17494 $
###############################################################################


#######################################
#The script is used to update project by batch command:
#SCADEDisplayConsole batch update *.ept
#######################################


start_path = "C:/svnfiles/SDY_A661_R19/TCP_SDY/TCP_Simulator/Test_Data/BatchSim_Input/SDY_Objects"
# start_path = "C:/svnfiles/SDY_A661_R19/TCP_SDY/TCP_Integration/Models/03_Interactors/SDY_CircleArea_Center"
SCADE_Installation_Path = "C:/Esterel/SCADE19/i11/SCADE Display"

etp_path=[]

for d in os.walk("%s" % start_path):
	for f in glob(os.path.join(d[0], '*.etp')):
		etp_folder = re.sub(r'\\','/',f)
		etp_folder = re.sub(r'(.*)/\w+\.etp',r'\1',etp_folder)
		sgfx_files_list = glob("%s/*.sgfx" % etp_folder)
		if len(sgfx_files_list) > 0:
			etp_path.append(f)
# print etp_path

for file in etp_path:
	cmd = "\"" +SCADE_Installation_Path + "/bin/ScadeDisplayConsole.exe"+"\"" + " batch update " + "\""+file+"\""
	print (cmd)
	os.system("\""+cmd+"\"")
