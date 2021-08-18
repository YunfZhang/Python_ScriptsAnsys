import re
import glob
import subprocess
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import List, Dict, Any

in_path = "definitions.dgfx"
tree = ET.parse(in_path)
nodes = tree.getroot()

content_type = ""
content_constant = ""

# added imported
pycode = "import os\n"
pycode += "import scade.model.display as SDY\n\n\n"
pycode += "defs = SDY.GlobalDefinitions(["

#predefined basic values
type_list = [
    "BOOL",
    "CHAR",
    "INT",
    "INT8",
    "INT16",
    "INT32",
    "INT64",
    "UINT8",
    "UINT16",
    "UINT32",
    "UINT64",
    "REAL",
    "FLOAT32",
    "FLOAT64",
    "WCHAR",
]

def parse_enum(def_value:str) -> str:
    enum_value = re.sub(r'enum {(.*)}',r'\1',def_value)
    temp_content = f'definition = SDY.EnumType(enums = ['
    if "," in enum_value:
        for v in enum_value.split(", "):
            temp_content += f'SDY.EnumValue(name = "{v}"),'
    else:
        temp_content += f'SDY.EnumValue(name = "{enum_value}"),'
    temp_content += ']),\n'
    return temp_content

def parse_imported(def_value:str) -> str:
    imported_name = def_value[len("imported "):]
    temp_content = f'definition = SDY.ImportedType(name = "{imported_name}"),\n'
    return temp_content

def parse_array(def_value:str) -> str:
    type_t = def_value.split("^", 1)[0].upper() #type: ignore
    type_d = def_value.split("^", 1)[1]
    temp_content = f'definition = SDY.ArrayType(SDY.PredefType(SDY.SimpleType.{type_t}), SDY.LiteralExpr("{type_d}")),\n'
    return temp_content

def parse_basic(def_value:str) -> str:
    temp_content = f'definition = SDY.PredefType(SDY.SimpleType.{def_value.upper()}),\n'#type: ignore
    return temp_content

def parse_structure(attr_name:str, def_value:str) -> str:
    temp_content = f"{attr_name} = SDY.StructType(["
    structure_value = re.sub(r'{(.*)}',r'\1',def_value)
    # print (f"the value is {structure_value}")
    struct_defs = structure_value.split(", ")
    for str_def in struct_defs:
        # print (f"the value is {str_def}")
        struct_name, struct_value = str_def.split(": ",1)
        if struct_value.startswith("{"):
            f_type = parse_structure("ty", struct_value)
        elif "^" in struct_value:
            n = struct_value.split("^",1)[0].upper()#type: ignore
            t = struct_value.split("^",1)[1]
            f_type = f'ty = SDY.ArrayType(SDY.PredefType(SDY.SimpleType.{n}), SDY.LiteralExpr("{t}")),'
        elif struct_value.upper() in type_list:#type: ignore
            f_type = f'ty = SDY.PredefType(SDY.SimpleType.{struct_value.upper()}),'#type: ignore
        else:
            f_type = f'ty = SDY.NamedType("{struct_value}"),'
        temp_content += f'SDY.StructFieldType(name = "{struct_name}", {f_type}),'
    temp_content = temp_content.rstrip(',') + "])\n"
    return temp_content

def get_definition(def_str:str)->str:
    def_content = ""
    if def_str.startswith("{"):#type: ignore #deal with structure type
        def_content += parse_structure("definition", def_str) #type:ignore
    elif def_str.startswith("imported"): #deal with imported type
        def_content += parse_imported(def_str) #type:ignore
    elif def_str.startswith("enum"): #deal with enum type
        def_content += parse_enum(def_str) #type:ignore
    else:
        if "^" in def_str:  #deal with array type
            def_content += parse_array(def_str)
        else:   #deal with basic type
            def_content += parse_basic(def_str)
    return def_content

for node in nodes:
    if node.tag == "type":
        type_name = node.attrib.get("name")
        type_oid = node.attrib.get("oid")
        content_type += f'SDY.TypeDefinition(name = "{type_name}", oid = "{type_oid}", '
        type_definition = node.find("./").text #type: ignore
        if type_definition:
            content_type += get_definition(type_definition)
        else:
            print ("the type definition is empty")
        content_type += '), '
    elif node.tag == "constant":
        const_name = node.attrib.get("name")
        const_oid = node.attrib.get("oid")
        const_type = node.attrib.get("type")
        const_init = node.find("./").text #type: ignore
        content_constant += "SDY.ConstantDefinition("
        content_constant += f'name="{const_name}", oid="{const_oid}", '
        if const_type.upper() in type_list:#type: ignore
            content_constant += f'type=SDY.PredefType(SDY.SimpleType.{const_type.upper()}), '#type: ignore
        else:
            content_constant += f'type=SDY.NamedType("{const_type}"), '
        if const_init:
            if re.match(r'\w+',const_init):
                content_constant += f'definition=SDY.LiteralExpr("{const_init}")'
            else:
                content_constant += f'definition=SDY.parse_expr("{const_init}"),'
        else:
            print ("the constant init value is empty")
        content_constant += "),"
    else:
        print (f"unknown  tag: {node.tag}")


pycode += content_type + content_constant
pycode += "])\n"
pycode += "output_path = 'Outputs/out_definition_2.dgfx'\n"
pycode += "os.makedirs(os.path.dirname(output_path), exist_ok=True)\n"
pycode += "SDY.save_dgfx(defs, output_path)\n"


out_path = "Outputs/out_dgfx.py"
with open(out_path, "w") as f:
    f.write(pycode)
print(f"Wrote {out_path} succesfully!")
subprocess.call(f"python -m black {out_path}")