import os
import re
from glob import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom
import shutil


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

#get the configuration of TC_IDs
#and also return the related source of the configuration ID
def get_conf_tc(node):
	TC_IDs = dict()
	for child in node:
		if re.match(r'Conf_TC',child.get('name'),re.I):
			props_Node = find_node(tree_etp, './props')
			for prop_child in props_Node:
				if (prop_child.get('name') == "@SDY:CONFSOURCE"):
					for prop_child_child in prop_child:
						if (prop_child_child.tag == "value"):
							if (prop_child[1].text == child.get('id')):
								TC_IDs[child.get('name')] = prop_child[0].text
	return TC_IDs

#function to find existed html files, which is existed test case html file
def get_existed_htm(path):
	htmls = glob("%s/../*.htm" %path)
	return htmls

#function to parse sgfx	
def read_sgfx(in_path):
	tree = ET.parse(in_path)
	return tree

#function to get ogfx name from given nodes
#return a list
def get_ogfx_name(nodes):
	ogfx_name_dict= []
	for node in nodes:
		for sub_node in node:
			if sub_node.tag == "properties": 
				ogfx_name_dict.append(sub_node.get('name'))
	return ogfx_name_dict

#function to read an existed html file and write it to new html file
def read_write_htm(src, dst, ogfx_file, conf_id,tc_id_dst):
	content = ""
	with open(src, 'r') as f_r:
		for line in f_r:
			line = re.sub(r'(SDY_SIMULATOR_TC_[N|R]_\d+)',r''+tc_id_dst+'',line)
			line = re.sub(r'(Conf_TC_[N|R]_\d+)',r''+conf_id+'',line)
			line = re.sub(r'(\w+\.sgfx)',r''+ogfx_file+'.ogfx',line)
			content += line
	with open(dst, 'w') as f_w:
		f_w.write(content)

	
	

	
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
		proj_folder = re.sub(r'(.*)\\(\w+.etp)',r'\1',etp)
		proj_name = re.sub(r'(.*)\\(\w+.etp)',r'\2',etp)
		
		
		#######################################################
		print ("\n\n#############################################")
		print ("Start to generated html for project: %s" %proj_name)
		print ("#############################################\n\n")
		#######################################################
		tree_etp = read_etp(etp)
		FileRef_Node = find_nodes(tree_etp, './roots/Folder')
		ogfx_sources = get_source(FileRef_Node)
		configurations_node = find_node(tree_etp,'./configurations')
		Conf_IDs = get_conf_tc(configurations_node)
		
		print (Conf_IDs)
		
		#get all ogfx file from sgfx
		#to tell which ogfx is generated from which sgfx
		ogfx_in_sgfx = {}
		for sgfx in sgfx_list:
			ogfx_name_list=[]
			sgfx_folder = re.sub(r'(.*)\\(\w+.sgfx)',r'\1',sgfx)
			sgfx_name = re.sub(r'(.*)\\(\w+.sgfx)',r'\2',sgfx)
			ogfx_name_list.append(re.sub(r'(\w+).sgfx',r'\1_ogfx',sgfx_name))
			ogfx_in_sgfx[sgfx] = ogfx_name_list

		print (ogfx_in_sgfx)
		number=0
		#get existed html file list from project path
		htm_list=get_existed_htm(proj_folder);
		
		for sgfx_keys, ogfx_values in ogfx_in_sgfx.items():
			html_sgfx = re.sub(r'\\','/',sgfx_keys)
			html_sgfx = re.sub(r'(.*)/(\w+\.sgfx)',r'\2', html_sgfx)
			
			#######################################################
			print ("\n\n------------------------------------------------")
			print ("Start to generated html for sgfx: %s" %html_sgfx)
			print ("------------------------------------------------\n\n")
			#######################################################
			dst_html=""
			tc_id_src_list=[]
			
			#get the existed TC ID from the given sgfx
			for conf, source in Conf_IDs.items():
				if source == html_sgfx:
					tc_id_src = re.sub(r'Conf_(\w+)',r'SDY_SIMULATOR_\1',conf)
					tc_id_src_list.append(tc_id_src)
			for ogfx in ogfx_values:
				for conf2,source2 in Conf_IDs.items():
					if re.match(r'\w+.ogfx', source2) and (ogfx in source2):
						number += 1
						tc_id_dst = re.sub(r'Conf_(\w+)',r'SDY_SIMULATOR_\1',conf2)
						if (number % 2 == 0):
							html_src = proj_folder + '/../' + tc_id_src_list[1]+'.htm'
							html_dst = re.sub(r'\\','/',html_src)
							html_dst = re.sub(r'(.*)/(\w+\.htm)',r'\1'+'/'+tc_id_dst+'.htm',html_dst)
							read_write_htm(html_src,html_dst,ogfx,conf2,tc_id_dst)
							print(html_src)
							print(html_dst)
						if (number % 2 == 1):
							html_src = proj_folder + '/../' + tc_id_src_list[0]+'.htm'
							html_dst = re.sub(r'\\','/',html_src)
							html_dst = re.sub(r'(.*)/(\w+\.htm)',r'\1'+'/'+tc_id_dst+'.htm',html_dst)
							read_write_htm(html_src,html_dst,ogfx,conf2,tc_id_dst)
			#######################################################
			print ("\n\n-------------------------------------------")
			print ("Start to generated html for sgfx: %s" %html_sgfx)
			print ("-------------------------------------------\n\n")
			#######################################################
		#######################################################
		print ("\n\n#############################################")
		print ("End of generation html for project: %s" %proj_name)
		print ("#############################################\n\n")
		#######################################################			
			
		
		
			
		

		



