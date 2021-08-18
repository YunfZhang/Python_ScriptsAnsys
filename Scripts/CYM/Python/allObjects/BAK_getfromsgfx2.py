import os
import re
import glob
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import List, Dict, Any


def prettify(elem: ET.Element) -> str:
    """Print result of a XML tree in a pretty way"""
    reparsed = minidom.parseString(ET.tostring(elem, "utf-8"))
    return "\n".join(
        [
            line
            for line in reparsed.toprettyxml(indent=" " * 2).split("\n")
            if line.strip()
        ]
    )


in_path = "specification_1.sgfx"
tree = ET.parse(in_path)
nodes = tree.getroot()

# added imported
pycode = "import os\n"
pycode += "import scade.model.display as SDY\n\n\n"

# added layer
layer_node = nodes.find("./children/layer")
layer_oid = layer_node.get("oid")  # layer oid: ignore #(all layer has <oid>)
pycode += f"layer = SDY.Layer(name = 'symbology_layer1', oid = '{layer_oid}', ratio = (1.0, 1.0), origin = (0.0, 0.0))\n"
pycode += "model = SDY.Specification(width = 768, height = 768, layers = [layer])\n\n\n"


# representation types
rep_list = [
    "line_width",
    "line_stipple",
    "line_cap",
    "color",
    "opacity",
    "index",
    "horizontal_alignment",
    "vertical_alignment",
    "font",
    "texture",
    "gradient",
    "as_string",
    "as_int_array",
    "as_multiline_string",
    "as_rich_string",
]
# var types
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

declaration_node = nodes.findall("./children/layer/declaration/")

for dec in declaration_node:
    output_str = ""
    # print(dec.tag)
    if "localConstant" in dec.tag:
        pycode += f"{dec.tag} = layer.declaration.local_constant\n"
    else:
        pycode += f"{dec.tag} = layer.declaration.{dec.tag[0:-1]}\n"
    for d in dec.findall("./"):
        # print(d.tag)
        var_memory = d.get("memory")
        var_name = d.get("name")
        var_oid = d.get("oid")
        var_representation = d.get("representation")
        var_type = d.get("type")
        var_init_value = d.find("init").text  # type: ignore #(all have <init>)

        if var_memory:
            # added memory if it is output
            output_str += f"{dec.tag}.append(SDY.MemVariable(name = '{var_name }', "
            # added name
            output_str += f"memory = SDY.MemVariable('{var_memory}'), "
        else:
            output_str += f"{dec.tag}.append(SDY.Variable(name = '{var_name }', "
        output_str += f"oid = '{var_oid}', "
        # added the representation if there is representation
        if var_representation in rep_list:
            output_str += (
                f"representation = SDY.Representation.{var_representation.upper()}, "
            )
        # added the type
        # this is basic type
        if var_type.upper() in type_list:
            output_str += f"type = SDY.PredefType(SDY.SimpleType.{var_type.upper()}), "
            # added the init value for simple type
            output_str += f"init = SDY.LiteralExpr('{var_init_value}')))\n"
        # this is array type
        elif "^" in var_type:
            type_t = var_type.split("^", 1)[0].upper()
            type_d = var_type.split("^", 1)[1]
            if type_t.upper() in type_list:
                output_str += f"type = SDY.ArrayType(SDY.PredefType(SDY.SimpleType.{type_t}), SDY.LiteralExpr('{type_d}')), "
            else:
                output_str += f"type = SDY.NamedType('{var_type}'), "
            # added the init value for array type
            output_str += f"init = SDY.parse_expr('{var_init_value}')))\n"
        # this is predefined type (ex: defined in dgfx)
        else:
            output_str += f"type = SDY.NamedType('{var_type}'), "
            output_str += f"init = SDY.parse_expr('{var_init_value}')))\n"

    pycode += f"{output_str}\n\n"
    # for d in ET.SubElement(dec,'/'):
    # print ('a')


object_str = ""
# start to get objects
groups_list = [
    "container",
    "panelContainer",
    "condContainer",
    "translationContainer",
    "rotationContainer",
    "filterTranslationContainer",
    "filterRotationContainer",
]
object_property_ignore_list = [
    "texture",
    "visible",
    "modulate",
    "lineCap",
    "polygonSmooth",
    "gradient",
    "tessellate",
    "enable",
    "textureControl",
    "priority",
    "static",
    "startRotationLocked",
    "endRotationLocked",
    "startTranslationLocked",
    "endTranslationLocked",
]

def getobjectcontent(object_nodes: List[ET.Element], parent = "layer") -> str:
    """Return string corresponding to objects"""
    mycontentstr = ""
    for objs in object_nodes:
        top_object_oid = objs.get("oid")
        top_object_name = objs.tag
        obj_nodes = objs.findall("./")
        for obj_node in obj_nodes:
            print(f"\n-------------------------{obj_node.tag}---------------------------\n\n")
            if obj_node.tag == "properties":
                obj_name = obj_node.get("name")
                #added content to python script
                mycontentstr += f"{obj_name} = SDY.{top_object_name.capitalize()}( "
                mycontentstr += f"name = '{obj_name}', oid = '{top_object_oid}', "
                property_nodes = obj_node.findall("./")
                for pro_node in property_nodes:
                    # attr = re.sub(r'(\w)([A-Z])', r'\1_\2', pro_node.tag).lower()
                    if pro_node.tag in object_property_ignore_list:
                        pass
                    elif pro_node.tag == "startAngle":
                        pro_node_start_init = pro_node.find("./angle/init").text
                        mycontentstr += f"start_angle = {pro_node_start_init}, "
                    elif pro_node.tag == "endAngle":
                        pro_node_end_init = pro_node.find("./angle/init").text
                        mycontentstr += f"end_angle = {pro_node_end_init}, "
                    elif pro_node.tag == "rotate":
                        pro_node_rotate_init = pro_node.find("./angle/init").text
                        mycontentstr += f"angle = {pro_node_rotate_init}, "
                    elif pro_node.tag == "center":
                        pro_node_centerx_init = pro_node.find("./x/init").text
                        pro_node_centery_init = pro_node.find("./y/init").text
                        mycontentstr += f"{pro_node.tag} = ({pro_node_centerx_init}, {pro_node_centery_init}), "
                    elif pro_node.tag == "origin":
                        pro_node_originx_init = pro_node.find("./x/init").text
                        pro_node_originy_init = pro_node.find("./y/init").text
                        mycontentstr += f"{pro_node.tag} = ({pro_node_originx_init}, {pro_node_originy_init}), "
                    elif pro_node.tag == "scale":
                        pro_node_scalex_init = pro_node.find("./x/init").text
                        pro_node_scaley_init = pro_node.find("./y/init").text
                        mycontentstr += f"{pro_node.tag} = ({pro_node_scalex_init}, {pro_node_scaley_init}), "
                    elif pro_node.tag == "orientation":
                        if pro_node.attrib.get('clockwise') == "false":
                            mycontentstr += f"clockwise = False, "
                        else:
                            mycontentstr += f"clockwise = True, "
                    # elif pro_node.tag in ["lineWidth", "lineStippe"]:
                        # init = pro_node.find("./init").text
                        # mycontentstr += f"{attr} = {init}, "
                    elif pro_node.tag == "lineWidth":
                        init = pro_node.find("./init").text
                        mycontentstr += f"line_width = {init}, "
                    elif pro_node.tag == "lineStipple":
                        init = pro_node.find("./init").text
                        mycontentstr += f"line_stipple = {init}, "
                    elif pro_node.tag == "outlineColor":
                        init = pro_node.find("./init").text
                        mycontentstr += f"outline_color = {init}, "
                    elif pro_node.tag == "haloColor":
                        init = pro_node.find("./init").text
                        mycontentstr += f"halo_color = {init}, "
                    elif pro_node.tag == "fillColor":
                        init = pro_node.find("./init").text
                        mycontentstr += f"fill_color = {init}, "
                    elif pro_node.tag == "outlineOpacity":
                        init = pro_node.find("./init").text
                        mycontentstr += f"outline_opacity = {init}, "
                    elif pro_node.tag == "fillOpacity":
                        init = pro_node.find("./init").text
                        mycontentstr += f"fill_opacity = {init}, "
                    else:
                        init = pro_node.find("./init").text
                        if init == "false":
                            mycontentstr += f"{pro_node.tag} = False, "
                        elif init == "true":
                            mycontentstr += f"{pro_node.tag} = True, "
                        else:
                            mycontentstr += f"{pro_node.tag} = {init}, "
                mycontentstr +=")\n"
                mycontentstr = mycontentstr.replace(", )", ")")
                mycontentstr += f"{parent}.children.append({obj_name})\n" 
                print(f"\n\n******************is {mycontentstr}")
            elif obj_node.tag == "children" and len(list(obj_node)) > 0:
                print(f"{top_object_name} in elif != 0 loop\n")
                mycontentstr += getobjectcontent(obj_node, obj_name)
            else:
                pass
    return mycontentstr


#start to get object content
object_nodes = nodes.findall("children/layer/children/")
# for objects in object_nodes:
object_str = getobjectcontent(object_nodes)

pycode += object_str
# save the Specification to a given location
pycode += "output_path = 'Outputs/out_specification_1.sgfx'\n"
pycode += "os.makedirs(os.path.dirname(output_path), exist_ok=True)\n"
pycode += "SDY.save_sgfx(model, output_path)\n"

with open("Outputs/out.py", "w") as f:
    f.write(pycode)

xmlstr = minidom.parseString(ET.tostring(nodes)).toprettyxml(
    indent="    ", encoding="utf-8"
)
with open("Outputs/out2.sgfx", "wb") as f2:
    f2.write(xmlstr)
