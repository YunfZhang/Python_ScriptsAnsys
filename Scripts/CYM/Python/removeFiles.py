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

def find_node(tree, path):
	return(tree.find(path))

#use findall() return a list
def find_nodes(tree, path):
	return(tree.findall(path))
	
#function to parse sgfx	
def read_sgfx_etp(in_path):
	tree = ET.parse(in_path)
	return tree
	
def get_ogfx_name(nodes):
	ogfx_name_dict= []
	for node in nodes:
		for sub_node in node:
			if sub_node.tag == "properties": 
				ogfx_name_dict.append(sub_node.get('name'))
	return ogfx_name_dict

def remove_ogfx(sgfx_list):
	print ("start to remove ogfx file")
	ogfxs = []
	for sgfx in sgfx_list:
		sgfx = re.sub(r'\\','/',sgfx)
		sgfx_folder = re.sub(r'(.*)/(\w+.sgfx)',r'\1',sgfx)
		sgfx_name = re.sub(r'(.*)/(\w+.sgfx)',r'\2',sgfx)
		
		sgfx_tree = read_sgfx_etp(sgfx)
		container_node = find_nodes(sgfx_tree, './children/layer/children/container')
		ogfx_name_list = get_ogfx_name(container_node)
		for ogfx in ogfx_name_list:
			# print ("\n\n")
			ogfx = ogfx + ".ogfx"
			ogfxs.append(ogfx)
			ogfx_file = sgfx_folder + "/" + ogfx
			# print (ogfx_file)
			os.system("svn remove %s" %ogfx_file)
	return ogfxs
	
def remove_conf_inETP(etp,ogfx_list):
	print ("start to remove remove_conf_inETP")
	etp = re.sub(r'\\','/',etp)
	etp_folder = re.sub(r'(.*)/(\w+.etp)',r'\1',etp)
	etp_name = re.sub(r'(.*)/(\w+.etp)',r'\2',etp)
	etp_tree = read_sgfx_etp(etp)
	root = etp_tree.getroot()
	# print (Conf_IDs)
	FileRef = find_nodes(root,'./roots/Folder')
	print ("Start to remove referenced ogfx files:\n")
	for refs in FileRef:
		if re.match(r'.*Model files',refs.get('name'),re.I):
			for ogfx in ogfx_list:
				for ref in refs[0]:
					if ref.get('persistAs') in ogfx_list:
						refs[0].remove(ref)
	
	configurations_node = find_node(root,'./configurations')
	Conf_IDs = get_conf_tc(configurations_node)
	print ("Start to remove Config ID for referenced ogfx files:\n")
	id_confs=[]
	for conf in Conf_IDs:
		for conf_node in configurations_node:
			if conf_node.get('name') in Conf_IDs:
				# print (conf_node.get('name'))
				id_confs.append(conf_node.get('id'))
				configurations_node.remove(conf_node)
	# print (id_confs)
	# Remove CONFIGURATIONS
	prop_configurations = root.find("./props/Prop[@name='CONFIGURATIONS']")
	for value in prop_configurations[:]:
		if value.text in id_confs:
			prop_configurations.remove(value)
	# Remove Properties	
	prop_nodes = root.findall('./props/Prop')
	for prop in prop_nodes:
		# print (prop.tag )
		# print (prop.attrib )
		for pname in ["@SDY:CONFTARGET", "@SDY:CONFSOURCE", "@SDY:KCGTEMPLATE", "@SDY:CONFOUTPUT", "@SDY:POINTERID", "@SDY:KEYBOARDID"]:
			if (pname == prop.get('name')):
				for item in prop:
					if item.tag == 'configuration':
						if item.text in id_confs:
							root.find('./props').remove(prop)
	newET=ET.ElementTree(root)
	newETP = etp
	newET.write(newETP)

def get_conf_tc(node):
	tclist = []
	for child in node:
		if re.search (r'Conf_TC_',child.get('name')):
			if int(re.sub(r'Conf_TC_N_(\d+)',r'\1',child.get('name')))>250:
				tclist.append(child.get('name'))
	return tclist
	
def remove_html(etp_folder, nodes):
	Conf_IDs = get_conf_tc(nodes)
	print ("start to remove html file")
	for tc in Conf_IDs:
		tc = re.sub(r'Conf_(TC_N_\d+)',r'\1',tc)
		html = etp_folder + "/../" + "SDY_SIMULATOR_" + tc + ".htm"
		# print (html)
		os.system("svn remove %s" %html)
		

def remove_expected(etp_folder,nodes):
	Conf_IDs = get_conf_tc(nodes)
	print ("start to remove expected folder and sub file(s)")
	for tc in Conf_IDs:
		tc = re.sub(r'Conf_(TC_N_\d+)',r'\1',tc)
		expected_folder = etp_folder + "/../" + "Output/Expected_Results/" + "SDY_SIMULATOR_" + tc
		# print (expected_folder)
		os.system("svn remove %s" %expected_folder)
	
def start_to_remove(etp, sgfx_list):
	etp = re.sub(r'\\','/',etp)
	etp_folder = re.sub(r'(.*)/(\w+.etp)',r'\1',etp)
	etp_name = re.sub(r'(.*)/(\w+.etp)',r'\2',etp)
	etp_tree = read_sgfx_etp(etp)
	
	configurations_node = find_node(etp_tree,'./configurations')
	
	all_ogfx_name_list = remove_ogfx(sgfx_list)
	remove_html(etp_folder, configurations_node)
	remove_expected(etp_folder,configurations_node)
	remove_conf_inETP(etp,all_ogfx_name_list)
	

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
	
	#start to loop the project in the given path
	for etp,sgfx_list in projs_dict.items():
		# print (etp)
		# print (sgfx_list)
		
		start_to_remove(etp,sgfx_list)
	
			
		

		



