import os
import re
from glob import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom


###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date :		$Date: 2017-09-06 09:44:00 +0800 (周三, 06 9月 2017) $
# Revision:		$Revision: 17494 $
###############################################################################

def prettify(elem):
	'''Print result of a XML tree in a pretty way'''
	reparsed = minidom.parseString(ET.tostring(elem, 'utf-8'))
	return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

def get_etp_from_path(start_path):
	etp_path={}
	for d in os.walk("%s" % start_path):
		for f in glob(os.path.join(d[0], '*.etp')):
			etp_folder = re.sub(r'\\','/',f)
			etp_folder = re.sub(r'(.*)/\w+\.etp',r'\1',etp_folder)
			sgfx_files_list = glob("%s/*.sgfx" % etp_folder)
			if len(sgfx_files_list) > 0:
				etp_path[f]=sgfx_files_list
	return etp_path

def read_etp(in_path):
	tree = ET.parse(in_path)
	return tree

def find_node(tree, path):
	return(tree.find(path))

#use findall() return a list
def find_nodes(tree, path):
	return(tree.findall(path))

def get_source(node):
	source_ogfx = []
	for child in node:
		if re.match(r".*Model files",child.get('name'),re.I):
			for sub_child in child[0]:
				if re.match(r'\w+_ogfx.ogfx',sub_child.get('persistAs')):
					source_ogfx.append(sub_child.get('persistAs'))
	return source_ogfx

def add_props(tree, source, id):
	conf_id = id;
	prop_id = int(id)+1
	max_id = 0
	props = tree.find('.//props')
	for prop in props:
		if (prop.get('name') == 'CONFIGURATIONS'):
			ET.SubElement(prop, 'value').text = str(conf_id)
	for pname in ["@SDY:CONFTARGET", "@SDY:CONFSOURCE", "@SDY:KCGTEMPLATE", "@SDY:CONFOUTPUT", "@SDY:POINTERID", "@SDY:KEYBOARDID"]:
		prop = ET.SubElement(props, 'Prop', {'id':str(prop_id), 'name':pname})
		if (pname == "@SDY:CONFTARGET"):
			ET.SubElement(prop, 'value').text = 'Simulation'
		if (pname == "@SDY:CONFSOURCE"):
			ET.SubElement(prop, 'value').text = source
		if (pname == "@SDY:CONFOUTPUT"):
			ET.SubElement(prop, 'value').text = '%ModelName%_Simulation'
		if (pname == "@SDY:POINTERID"):
			ET.SubElement(prop, 'value').text = '0'
		if (pname == "@SDY:KEYBOARDID"):
			ET.SubElement(prop, 'value').text = '0'
		ET.SubElement(prop, 'configuration').text = str(conf_id)
		prop_id += 1
	max_id = prop_id
	# print (prettify(props))
	return max_id
	
def get_FileRef_Max_id(node):
	maxID=0
	for child in node:
		if ((child.get('name') == "Display Model files") or (child.get('name') == "Model Files")):
			for FileRef in child[0]:
				id = int(FileRef.get('id'))
				if id > maxID:
					maxID = id
	return maxID

if __name__ == "__main__":

	#Load Test Environment
	try: 
		import ENVIRONMENT as ENV
	except Exception as e: 
		raise Exception
		print ("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
		
	
	start_path = ENV.start_path
	SCADE_Installation_Path = ENV.SCADE_Installation_Path
	
	projs_dict = get_etp_from_path(start_path)
	TC_ID = 250
	
	for etp in projs_dict.keys():
		# print ("\n\n %s" %etp)
		proj_folder = re.sub(r'(.*)\\(\w+.etp)',r'\1',etp)
		proj_name = re.sub(r'(.*)\\(\w+.etp)',r'\2',etp)
		
		tree_etp = read_etp(etp)
		FileRef_Node = find_nodes(tree_etp, './roots/Folder')
		ogfx_sources = get_source(FileRef_Node)
		max_id=get_FileRef_Max_id(FileRef_Node)
		# print (ogfx_sources)
		Dec_Node = find_node(tree_etp,'./configurations')
		
		#run twice of each ogfx, one configuration for sss scenario and one for csv scenario
		for source in [item for item in ogfx_sources for i in range(2)]:
			TC_ID += 1
			max_id += 1
			tcid = "Conf_TC_N_"+str(TC_ID)
			ET.SubElement(Dec_Node, 'Configuration', {'id':str(max_id), 'name':tcid})
			max_id = add_props(tree_etp, source, max_id)
		# print("Dec_Node tostring: %s" %ET.tostring(Dec_Node))
		# print (prettify(Dec_Node))
		tree_etp.write(etp,encoding="utf-8", xml_declaration=True)
		
		print("--------------------------------------------------\n")
		cmd = "\"" +SCADE_Installation_Path + "/bin/ScadeDisplayConsole.exe"+"\"" + " batch update " + "\""+etp+"\""
		print (cmd)
		os.system("\""+cmd+"\"")
		print("\n--------------------------------------------------")
			
		

		



