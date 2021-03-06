#!python
import sys
import re
import os
from glob import glob
from subprocess import call

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date:				$Date: 2017-09-06 09:44:00 +0800 (周三, 06 9月 2017) $
# Revision:			$Revision: 17494 $
###############################################################################


#Command line example
#python Run_Integration_TC.py TC-SDY-Integration-05-14

#Load Test Environment
try: 
	import ENVIRONMENT as ENV
except Exception: 
	print("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
	raise

#Get the installation path
Installation_Path = ENV.Installation


###to check the installation path
SCADE_EXE = Installation_Path + "/SCADE/bin/SCADE.exe"
SCSSMLNC_EXE = Installation_Path + "/SCADE/bin/SCSSMLNC.exe"
ScadeDisplayCGSimu_EXE = Installation_Path + "/SCADE Display/bin/ScadeDisplayCGSimu.exe"
if not os.path.exists(SCADE_EXE):
	print ("The SCADE.exe is not find at: ".format(SCADE_EXE))
	quit()
if not os.path.exists(ScadeDisplayCGSimu_EXE):
	print ("The ScadeDisplayCGSimu.exe is not find at: ".format(ScadeDisplayCGSimu_EXE))
	quit()


#Get the TC name from command line
# file_name = sys.argv[0]
# TC_Name = re.sub(r'.py','',file_name)
is_valid_TCName = 0
TC_Name = sys.argv[1]
while not is_valid_TCName:
	if re.match(r'TC-SDY-.*-\d+',TC_Name):
		print ("The entered ID name is: {}".format(TC_Name))
		is_valid_TCName = 1
	else:
		TC_Name=raw_input("Please enter corrected TC ID (ex: TC-SDY-Integration-05-14):")

#List the TC ID generation type	
#There are three types: Standalone, CoGen, CoSim
tcDict = {	'Standalone':['TC-SDY-Integration-07','TC-SDY-CUT-Integration-07'],
			'CoGen':['TC-SDY-Integration-06','TC-SDY-CUT-Integration-06'],
			'CoSim':['TC-SDY-Integration-05']}
			
tcid = re.sub(r'(?<=\d{2})(-\d+)+', '', TC_Name)
tcType = None
for type, listTC in tcDict.items():			
	if tcid in listTC:
		tcType = type
	else:
		pass
if tcType is None:
	raise Exception("Type not found for %s" % TC_Name)
else:
	print("Type of '%s' is '%s'" % (TC_Name, tcType))
	

#check the TC status log file
TC_Status_Log = TC_Name+".log"
if os.path.exists(TC_Status_Log):
	os.remove(TC_Status_Log)
open(TC_Status_Log,'a').close()


TC_Input_Model_List = "./Input_Models/" + TC_Name + ".lst"
print (TC_Input_Model_List)
if os.path.exists(TC_Input_Model_List):
	print (TC_Input_Model_List)
else:
	print ("The TC: {}'s list file: {} is not exists".format(TC_Name, TC_Input_Model_List))
	quit()
		
with open(TC_Input_Model_List,'r') as start_file:
	list_Files = start_file.readlines()

Status_string = ""
if tcType == "CoSim":
	for myFile in list_Files:
		if not myFile.isspace():
			myFile = re.sub(r'\n','',myFile)
			currentPath = os.getcwd()
			ModelPath = currentPath + "/../../" + myFile
			ModelPath = re.sub(r'\\',r'/',ModelPath)
			ModelName = re.sub(r'(.*)/(\w+).etp',r'\2.etp',ModelPath)
			ModelFolder = re.sub(r'(.*)/(\w+).etp',r'\1',ModelPath)
			Status_string += "\n\n"
			Status_string += "****************Start test with model: "+ModelName
			if os.path.exists(ModelPath):
				cmd = SCADE_EXE + " -code " + "\""+ModelPath+"\""+" -root Operator1 -conf Simulation -sim -all"
				exit_code_build = call(cmd)
				dllFile = glob("%s/Simulation/*.dll" % ModelFolder)
				if(len(dllFile)>1):
					dllFile_dll = dllFile[0]
				else:
					dllFile_dll=""
				if (exit_code_build == 0) and (os.path.exists(dllFile_dll)):
					Status_string += "\nSimulation build on model: "+ModelName+" ==> Passed"
					Simulation_Status = "Passed"
					print ("The Simulation on model: {} is passed \n \n".format(ModelPath))
				else:
					Simulation_Status = "Failed"
					Status_string += "\nSimulation build on model: "+ModelName+" ===> Failed"
					print ("The Simulation on model: {} is failed \n\n".format(ModelPath))
				if Simulation_Status == "Passed":
					FolderPath = re.sub(r'(.*)/\w+.etp',r'\1',ModelPath)
					# list_Files = glob("%s/*/*.[so]gfx" % start_folder)
					dllPath = glob("%s/Simulation/*.dll" % FolderPath)
					# dllPath = FolderPath + "/Simulation/Operator1.dll"
					scenarioFile = FolderPath +"/"+ TC_Name+".sss"
					if(len(dllPath)>0):
						cmd_sim = SCSSMLNC_EXE +" "+ "\""+dllPath[0]+"\"" + " -scenario " + "\""+scenarioFile+"\"" + " -out "+"\""+FolderPath+"/a.out"+"\""
						exit_code_sim = call(cmd_sim)
					else:
						exit_code_sim=1
					if exit_code_sim == 0:
						cosim_Status = "Passed"
						Status_string += "\nCo-Simulation on model: "+ModelName+" ===> Passed"
						print ("The Co-simulation on model: {} is passed \n \n".format(ModelPath))
					else:
						cosim_Status = "Failed"
						Status_string += "\nCo-Simulation  on model: "+ModelName+" ===> Failed"
						print ("The Co-Simulation on model: {} is failed \n\n".format(ModelPath))
			else:
				Status_string += "\nThe path of model: "+ModelName+" is not existed"
				print ("sorry the file: {} does not exist",ModelPath)
			Status_string += "\n****************End of test with model: "+ModelName+"\n\n"
		else:
			print ("Skip the empty line")
			#do nothing on empty line
elif tcType == "Standalone":
	for myFile in list_Files:
		if not myFile.isspace():
			myFile = re.sub(r'\n','',myFile)
			currentPath = os.getcwd()
			ModelPath = currentPath + "/../../" + myFile
			ModelPath = re.sub(r'\\',r'/',ModelPath)
			ModelName = re.sub(r'(.*)/(\w+).etp',r'\2.etp',ModelPath)
			ModelFolder = re.sub(r'(.*)/(\w+).etp',r'\1',ModelPath)
			Status_string += "\n\n"
			Status_string += "****************Start test with model: "+ModelName
			if os.path.exists(ModelPath):
				cmd = SCADE_EXE + " -code " + "\""+ModelPath+"\""+" -root Operator1 -conf TestStandalone -sim -all"
				exit_code_build = call(cmd)
				standaloneFile = glob("%s/TestStandalone/*.exe" % ModelFolder)
				if(len(standaloneFile)>0):
					standaloneEXE = standaloneFile[0]
				else:
					standaloneEXE=""
				if (exit_code_build == 0) and (os.path.exists(standaloneEXE)):
					Status_string += "\Standalone generation on model: "+ModelName+" ==> Passed"
					Standalone_Status = "Passed"
					print ("The Standalone generation on model: {} is passed \n \n".format(ModelPath))
				else:
					Standalone_Status = "Failed"
					Status_string += "\nStandalone generation build on model: "+ModelName+" ===> Failed"
					print ("The Standalone generation on model: {} is failed \n\n".format(ModelPath))
			else:
				Status_string += "\nThe path of model: "+ModelName+" is not existed"
				print ("sorry the file: {} does not exist",ModelPath)
			Status_string += "\n****************End of test with model: "+ModelName+"\n\n"
		else:
			print ("Skip the empty line")
			#do nothing on empty line
elif tcType == "CoGen":
	for myFile in list_Files:
		if not myFile.isspace():
			myFile = re.sub(r'\n','',myFile)
			currentPath = os.getcwd()
			ModelPath = currentPath + "/../../" + myFile
			ModelPath = re.sub(r'\\',r'/',ModelPath)
			ModelName = re.sub(r'(.*)/(\w+).etp',r'\2.etp',ModelPath)
			ModelFolder = re.sub(r'(.*)/(\w+).etp',r'\1',ModelPath)
			Status_string += "\n\n"
			Status_string += "****************Start test with model: "+ModelName
			if os.path.exists(ModelPath):
				cmd = SCADE_EXE + " -code " + "\""+ModelPath+"\""+" -root Operator1 -conf TestCoGen"
				exit_code_build = call(cmd)
				
				CoGenFile = glob("%s/TestCoGen/*_adaptor.c" % ModelFolder)
				if(len(CoGenFile)>0):
					CoGenFile_C = CoGenFile[0]
				else:
					CoGenFile_C=""
				
				if (exit_code_build == 0) and (os.path.exists(CoGenFile_C)):
					Status_string += "\nCo-generation on model: "+ModelName+" ==> Passed"
					CoGen_Status = "Passed"
					print ("The Co-generation on model: {} is passed \n \n".format(ModelPath))
				else:
					CoGen_Status = "Failed"
					Status_string += "\nCo-generation build on model: "+ModelName+" ===> Failed"
					print ("The Co-generation on model: {} is failed \n\n".format(ModelPath))
			else:
				Status_string += "\nThe path of model: "+ModelName+" is not existed"
				print ("sorry the file: {} does not exist",ModelPath)
			Status_string += "\n****************End of test with model: "+ModelName+"\n\n"
		else:
			print ("Skip the empty line")
			#do nothing on empty line
else:
	pass
with open(TC_Status_Log,'w') as Status_file:
	Status_file.write(Status_string)
Status_string = ""