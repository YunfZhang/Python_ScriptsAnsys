from xml.etree import ElementTree as ET
from xml.dom import minidom

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date:				$Date: 2017-08-23 15:06:28 +0800 (周三, 23 8月 2017) $
# Revision:			$Revision: 17399 $
###############################################################################

def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ET.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

d1 = {'name':'leo', 'age':'age20', 'sex':'male'}
for keys,values in d1.items():
	#set the root
	root = ET.Element(keys)
	#set the <IDE> tag
	IDE=ET.SubElement(root, 'IDE')
	project_name = values+"C_Group.etp"
	ET.SubElement(IDE, 'ratio', {'horizontal':"1", 'vertical':"1"})
	ET.SubElement(IDE, 'project', {'path': project_name})
	symbology=ET.SubElement(root, 'symbology')
	ET.SubElement(symbology, 'ratio', {'height':"768", 'width':"768"})
	et=ET.ElementTree(root)
	file_name = keys+values+"_a.ogfx"
	print (ET.tostring(root))
	print ("\n\n")
	print (prettify(root))
	with open(file_name,"w") as f:
		f.write(prettify(root))
