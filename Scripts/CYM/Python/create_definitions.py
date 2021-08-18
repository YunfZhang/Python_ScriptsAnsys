import xml.etree.ElementTree as ET
from xml.dom import minidom
import random

basic = ['bool', 'char', 'float32', 'float64', 'int', 'int16', 'int32', 'int64', 'int8', 'real', 'uint16', 'uint32', 'uint64', 'uint8', 'wchar']
complextypes = ['array', 'structure', 'enumeration']

initial_dgfx = "definitions1.dgfx"
tree = ET.parse(initial_dgfx)
nodes = tree.getroot()
newtypes = list()
for t in basic:
    sub_type = ET.Element('type')
    type_name = 't_%s'%t
    sub_type.set('name', type_name)
    sub_type.set('oid', 'd8fb2292-0e01-475c-bdca-c3bce4c4620a')
    child = ET.Element('definition')
    child.text = t
    sub_type.append(child)
    nodes.append(sub_type)
    newtypes.append(type_name)

another_array = ""
another_str = ""
another_enum = ""
MAX_ELEMENT_VALUE = 10
MAX_DEMENSION_VALUE = 20
for i in range(1,MAX_DEMENSION_VALUE):
    another_array += "^" + str(random.randint(1,MAX_ELEMENT_VALUE))
    another_enum += "d{0}_{1}_{2}, "
    another_str += "{0}_{1}: {0}, "
    for k in range(1,MAX_ELEMENT_VALUE):
        for t in complextypes:
            for b in basic:
                sub_type = ET.Element('type')
                if t == "array":
                    type_name = "t_array_d{}_{}_{}".format(i, b, k)
                    type_text = b + another_array
                elif t == "structure": 
                    type_name = "t_struct_d{}_{}_{}".format(i, b, k)
                    type_text = another_str
                    type_text = type_text.format(b, str(k))
                    l1 = type_text.split(", ")
                    a1 = list()
                    for letter in range(97, 97+len(l1)-1):
                        a1.append(chr(letter))
                    for i in range(0,len(l1)-1):
                        l1[i] = l1[i].replace(":", "%s:"%a1[i]) 
                    type_text = ", ".join(l1)
                    type_text = "{%s}" % type_text
                    type_text = type_text.replace(", }","}")
                elif t == "enumeration": 
                    type_name = "t_enum_d{}_{}_{}".format(i, b, k)
                    type_text = another_enum
                    type_text = type_text.format(i, b, str(k))
                    l1 = type_text.split(", ")
                    a1 = list()
                    for letter in range(97, 97+len(l1)-1):
                        a1.append(chr(letter))
                    for i in range(0,len(l1)-1):
                        l1[i] = l1[i] + a1[i]
                    type_text = ", ".join(l1)
                    type_text = "enum {%s}" % type_text
                    type_text = type_text.replace(", }","}")
                else:
                    pass
                sub_type.set('name', type_name)
                sub_type.set('oid', 'd8fb2292-0e01-475c-bdca-c3bce4c4620a')
                child = ET.Element('definition')
                child.text = type_text
                sub_type.append(child)
                nodes.append(sub_type)
                newtypes.append(type_name)
for newtype in newtypes:
    sub_constant = ET.Element('constant')
    sub_constant.set('name', newtype.replace('t_','c_'))
    sub_constant.set('oid', 'd8fb2292-0e01-475c-bdca-c3bce4c4620a')
    sub_constant.set('type', newtype)
    child = ET.Element('init')
    child.text = "1"
    sub_constant.append(child)
    nodes.append(sub_constant)
    
    
xmlstr = minidom.parseString(ET.tostring(nodes)).toprettyxml(indent="    ", encoding="utf-8")
with open ("definitions_out3.dgfx", "wb") as f:
    f.write(xmlstr)
    
# et_write = ET.ElementTree(nodes)
# et_write.write("definitions_out.dgfx", encoding="utf-8", xml_declaration=True)
# et_write.write("definitions_out.dgfx")
