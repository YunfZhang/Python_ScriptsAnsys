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


###The script is used to create an ogfx file from layer

def prettify(elem):
	'''Print result of a XML tree in a pretty way'''
	reparsed = minidom.parseString(ET.tostring(elem, 'utf-8'))
	return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

def read_sgfx(in_path):
	tree = ET.parse(in_path)
	return tree

def write_ogfx(tree, out_path):
	tree.write(out_path, encoding='utf-8',xml_declaration=True)

def find_node(tree, path):
	return(tree.find(path))

#use findall() return a list
def find_nodes(tree, path):
	return(tree.findall(path))

def get_ogfx_name(nodes):
	ogfx_name_dict= {}
	for node in nodes:
		for sub_node in node:
			if sub_node.tag == "properties": 
				ogfx_name_dict[sub_node.get('name')] = node
	return ogfx_name_dict

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

def get_FileRef_Max_id(node):
	maxID=0
	for child in node:
		# if(child.get('name') == "Model Files"):
		if ((child.get('name') == "Display Model files") or (child.get('name') == "Model Files")):
			for FileRef in child[0]:
				id = int(FileRef.get('id'))
				if id > maxID:
					maxID = id
	return maxID

def create_node(tag, properties):
	element = ET.Element(tag, properties)
	return element
	
def add_element(nodelist, element):
	for node in nodelist:
		if ((node.get('name') == "Display Model files") or (node.get('name') == "Model Files")):
			node[0].append(element)
	
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
	
	for etp, sgfx_list in projs_dict.items():
		proj_name = re.sub(r'(.*)\\(\w+.etp)',r'\2',etp)
		ogfx_to_be_added_in_etp=[]
		print("\n--------------------------------------------------")
		print("Start to create ogfx on Project: %s" %proj_name)
		print("--------------------------------------------------\n")
		for sgfx in sgfx_list:
			sgfx_name = re.sub(r'(.*)\\(\w+.sgfx)',r'\2',sgfx)
			sgfx_path = re.sub(r'(.*)\\(\w+.sgfx)',r'\1',sgfx)
			print("\n--------------------------------------------------")
			print("Start to create ogfx from SGFX: %s" %sgfx_name)
			print("--------------------------------------------------\n")
			tree = read_sgfx(sgfx)
			#find declaration node
			dec_node = find_node(tree, './children/layer/declaration')
			
			container_node = find_nodes(tree, './children/layer/children/container')
			ogfx_name = re.sub(r'(\w+).sgfx',r'\1_ogfx',sgfx_name)
			# print ("ogfx name is: %s\n" %ogfx_name)
			root = ET.Element('object')
			IDE=ET.SubElement(root, 'IDE')
			ET.SubElement(IDE, 'ratio', {'horizontal':"1", 'vertical':"1"})
			ET.SubElement(IDE, 'project', {'path': proj_name})
			symbology=ET.SubElement(root, 'symbology')
			ET.SubElement(symbology, 'dimension', {'height':"768", 'width':"768"})
			declaration=ET.SubElement(root, 'declaration')
			declaration.extend(dec_node)
			children=ET.SubElement(root, 'children')
			group_container=ET.SubElement(children, 'container',{'oid':"c09e59ac-8809-45be-8047-fd9e16668ed2"})
			group_pathFromRoot = ET.SubElement(group_container, 'pathFromRoot',{'value':'0'} )
			group_properties = ET.SubElement(group_container, 'properties',{'name':'group'})
			for group_prop in ['visible','origin','priority','scale','rotate','orientation','static']:
				if group_prop == 'visible':
					group_properties_visible = ET.SubElement(group_properties, 'visible')
					group_properties_visible_init = ET.SubElement(group_properties_visible, 'init')
					group_properties_visible_init.text = "true"
				if group_prop == 'origin':
					group_properties_origin = ET.SubElement(group_properties, 'origin')
					group_properties_origin_x = ET.SubElement(group_properties_origin, 'x')
					group_properties_origin_x_init = ET.SubElement(group_properties_origin_x, 'init')
					group_properties_origin_x_init.text = "0.0"
					group_properties_origin_y = ET.SubElement(group_properties_origin, 'y')
					group_properties_origin_y_init = ET.SubElement(group_properties_origin_y, 'init')
					group_properties_origin_y_init.text = "0.0"
				if group_prop == 'priority':
					group_properties_priority = ET.SubElement(group_properties, 'priority')
					group_properties_priority_init = ET.SubElement(group_properties_priority, 'init')
					group_properties_priority_init.text = "-1"
				if group_prop == 'scale':
					group_properties_scale = ET.SubElement(group_properties, 'scale')
					group_properties_scale_x = ET.SubElement(group_properties_scale, 'x')
					group_properties_scale_x_init = ET.SubElement(group_properties_scale_x, 'init')
					group_properties_scale_x_init.text = "1.0"
					group_properties_scale_y = ET.SubElement(group_properties_scale, 'y')
					group_properties_scale_y_init = ET.SubElement(group_properties_scale_y, 'init')
					group_properties_scale_y_init.text = "1.0"
				if group_prop == 'rotate':
					group_properties_rotate = ET.SubElement(group_properties, 'rotate')
					group_properties_rotate_angle = ET.SubElement(group_properties_rotate, 'angle')
					group_properties_rotate_angle_init = ET.SubElement(group_properties_rotate_angle, 'init')
					group_properties_rotate_angle_init.text = "0.0"
				if group_prop == 'orientation':
					group_properties_orientation = ET.SubElement(group_properties, 'orientation',{'clockwise':'false'})
				if group_prop == 'static':
					group_properties_static = ET.SubElement(group_properties, 'static',{'editorLinked':'true', 'generateStaticSequence':'true', 'maxX':'0.0', 'maxY':'0.0', 'minX':'0.0', 'minY':'0.0'})
					group_properties_static_init = ET.SubElement(group_properties_static, 'init')
					group_properties_static_init.text = "false"
			# group_properties_visible = ET.SubElement(group_properties, 'visible')
			# group_value = ET.SubElement(container, 'visible')
			# group_value_init = ET.SubElement(group_value)
			
			group_children = ET.SubElement(group_container, 'children')
			group_children.extend(container_node)
			file_name = sgfx_path + "/" + ogfx_name + ".ogfx"
			ogfx_to_be_added_in_etp.append(file_name)
			with open(file_name,"w") as f:
				f.write(prettify(root))
			print("\n--------------------------------------------------")
			print("End of create ogfx from SGFX: %s" %sgfx_name)
			print("--------------------------------------------------\n")
		
		print("\n--------------------------------------------------")
		print("End of create ogfx on Project: %s" %proj_name)
		print("--------------------------------------------------\n")
		print("\n--------------------------------------------------")
		print("Start to add generated ogfx into etp: %s" %proj_name)
		print("--------------------------------------------------\n")
		tree_etp = read_sgfx(etp)
		# print("tree_etp tostring: %s" %ET.tostring(tree_etp))
		FileRef_node = find_nodes(tree_etp, './roots/Folder')
		max_id=get_FileRef_Max_id(FileRef_node)
		
		#added ogfx file in etp
		max_id += 100
		for b in ogfx_to_be_added_in_etp:
			ref_ogfx_name = re.sub(r'\\','/',b)
			ref_ogfx_name = re.sub(r'(.*)/(\w+.ogfx)',r'\2',ref_ogfx_name)
			elements = create_node('FileRef', {'id':str(max_id), 'persistAs':ref_ogfx_name})
			add_element(FileRef_node,elements)
			max_id += 1
		file_name2 = etp
		tree_etp.write(file_name2,encoding="utf-8", xml_declaration=True)
		print("\n--------------------------------------------------")
		print("End of add generated ogfx into etp: %s" %proj_name)
		print("--------------------------------------------------\n")
		
		print("\n--------------------------------------------------")
		print("Start to batch update on project: %s" %proj_name)
		print("--------------------------------------------------\n")
		cmd = "\"" +SCADE_Installation_Path + "/bin/ScadeDisplayConsole.exe"+"\"" + " batch update " + "\""+etp+"\""
		print (cmd)
		os.system("\""+cmd+"\"")
		print("\n--------------------------------------------------")
		print("End of batch update on project: %s" %proj_name)
		print("--------------------------------------------------\n")

	

		
		
