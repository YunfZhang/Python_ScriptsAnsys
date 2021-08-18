import os
import re
import glob
import subprocess
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


in_path = "specification.sgfx"
tree = ET.parse(in_path)
nodes = tree.getroot()

# added imported
pycode = "import os\n"
pycode += "import scade.model.display as SDY\n\n\n"

# added layer
layer_node = nodes.find("./children/layer")
layer_oid = layer_node.get("oid")  # type: ignore #(all layer has <oid>)
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
    "maxLength",
    "format",
    "maskActivity",
    "indexes", #why? conditional container
    "startTranslationValue",#why?
    "endTranslationValue", #why?
    "functionalTranslationValue", #why?
    "functionalRotationValue",
    "startRotationValue", #why?
    "endRotationValue", #why?
    "relative",
    "output",
    "restoreStates",
    "memory",
    "crc",
    "arcSegment",
]

def get_text(node: ET.Element, path:str) -> str:
    """Get value of XPath"""
    subnode = node.find(path)
    if hasattr(subnode, 'text'):
        return subnode.text  # type: ignore
    else:
        print(f"WARNING: {path}.text not found!")
        return ""

def getobjectcontent(object_nodes: List[ET.Element], parent = "layer") -> str:
    """Return string corresponding to objects"""
    mycontentstr = ""
    for objs in object_nodes:
        top_object_oid = objs.get("oid")
        top_object_name = objs.tag
        # print(f"\n\n---------------{top_object_name}------------------\n\n")
        obj_nodes = objs.findall("./")
        for obj_node in obj_nodes:
            if obj_node.tag == "properties":
                obj_name = obj_node.get("name").replace("-","")
                if " " in obj_name:
                    obj_name_nospace = re.sub(r'\ ', '',obj_name)
                else:
                    obj_name_nospace = obj_name
                #added content to python script
                mycontentstr += f"{obj_name_nospace} = SDY.{top_object_name[0].upper()+top_object_name[1:]}( "
                mycontentstr += f"name = '{obj_name}', oid = '{top_object_oid}', "
                property_nodes = obj_node.findall("./")
                for pro_node in property_nodes:
                    # attr = re.sub(r'(\w)([A-Z])', r'\1_\2', pro_node.tag).lower()
                    if pro_node.tag in object_property_ignore_list:
                        pass
                    elif pro_node.tag == "startAngle":
                        pro_node_start_init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"start_angle = {pro_node_start_init}, "
                    elif pro_node.tag == "startRotationAngle":
                        pro_node_start_init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"start_angle = {pro_node_start_init}, "
                    elif pro_node.tag == "endAngle":
                        pro_node_end_init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"end_angle = {pro_node_end_init}, "
                    elif pro_node.tag == "endRotationAngle":
                        pro_node_end_init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"end_angle = {pro_node_end_init}, "
                    elif pro_node.tag == "rotate":
                        pro_node_rotate_init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"angle = {pro_node_rotate_init}, "
                    elif pro_node.tag == "horzRadius" or pro_node.tag == "vertRadius" :
                        if pro_node.tag == "horzRadius":
                            horzRadius = get_text(pro_node, "./init")
                            mycontentstr += f"radius = ({horzRadius},"
                        else:
                            vertRadius = get_text(pro_node, "./init")
                            mycontentstr += f" {vertRadius}), "
                    elif pro_node.tag == "position":
                        fpx = get_text(pro_node, "./x/init")
                        fpy = get_text(pro_node, "./y/init")
                        if top_object_name == "bitmap" or top_object_name == "richText" or top_object_name == "text" or top_object_name == "biFont":
                            mycontentstr += f"position = ({fpx}, {fpy}), "
                        else:
                            mycontentstr += f"center = ({fpx}, {fpy}), "
                    elif pro_node.tag == "cursorPosition":
                        fpx = get_text(pro_node, "./x/init")
                        fpy = get_text(pro_node, "./y/init")
                        mycontentstr += f"position = ({fpx}, {fpy}), "
                    elif pro_node.tag == "firstPoint":
                        fpx = get_text(pro_node, "./x/init")
                        fpy = get_text(pro_node, "./y/init")
                        mycontentstr += f"first_point = ({fpx}, {fpy}), "
                    elif pro_node.tag == "refPoint":
                        refx = get_text(pro_node, "./x/init")
                        refy = get_text(pro_node, "./y/init")
                        mycontentstr += f"ref_point = ({refx}, {refy}), "
                    elif pro_node.tag == "startTranslationPoint":
                        refx = get_text(pro_node, "./x/init")
                        refy = get_text(pro_node, "./y/init")
                        mycontentstr += f"start_point = ({refx}, {refy}), "
                    elif pro_node.tag == "endTranslationPoint":
                        refx = get_text(pro_node, "./x/init")
                        refy = get_text(pro_node, "./y/init")
                        mycontentstr += f"end_point = ({refx}, {refy}), "
                    elif pro_node.tag == "thirdPoint" :
                        tpx = get_text(pro_node, "./x/init")
                        tpy = get_text(pro_node, "./y/init")
                        mycontentstr += f"third_point = ({tpx}, {tpy}), "
                    elif pro_node.tag == "clipStartPoint" :
                        tpx = get_text(pro_node, "./x/init")
                        tpy = get_text(pro_node, "./y/init")
                        mycontentstr += f"start_point = ({tpx}, {tpy}), "
                    elif pro_node.tag == "clipAngle" :
                        anglev = get_text(pro_node, "./angle/init")
                        mycontentstr += f"angle = {anglev}, "
                    elif pro_node.tag == "center":
                        pro_node_centerx_init = get_text(pro_node, "./x/init")
                        pro_node_centery_init = get_text(pro_node, "./y/init")
                        mycontentstr += f"{pro_node.tag} = ({pro_node_centerx_init}, {pro_node_centery_init}), "
                    elif pro_node.tag == "origin":
                        pro_node_originx_init = get_text(pro_node, "./x/init")
                        pro_node_originy_init = get_text(pro_node, "./y/init")
                        mycontentstr += f"{pro_node.tag} = ({pro_node_originx_init}, {pro_node_originy_init}), "
                    elif pro_node.tag == "scale":
                        pro_node_scalex_init = get_text(pro_node, "./x/init")
                        pro_node_scaley_init = get_text(pro_node, "./y/init")
                        mycontentstr += f"{pro_node.tag} = ({pro_node_scalex_init}, {pro_node_scaley_init}), "
                    elif pro_node.tag == "points":
                        mycontentstr += f"{pro_node.tag} = ["
                        points_nodes = pro_node.findall("./")
                        for point in points_nodes:
                            if point.tag == "point": #ignore the arcSegment case
                                x_init = get_text(point, "./x/init")
                                y_init = get_text(point, "./y/init")
                                mycontentstr += f"({x_init}, {y_init}), "
                            else:
                                pass
                        mycontentstr += "], "
                    elif pro_node.tag == "inputParameters":
                        mycontentstr += f"inputs = ["
                        parameters = pro_node.findall("./")
                        for para in parameters:
                            para_name = para.attrib.get("name")
                            para_type = para.attrib.get("type")
                            para_oid = para.attrib.get("oid")
                            if "^" in para_type:
                                t_array = para_type.split("^", 1)# type: ignore
                                mycontentstr += f"('{para_name}', '{para_oid}', SDY.ArrayType(SDY.PredefType(SDY.SimpleType.{t_array[0].upper()}), SDY.LiteralExpr('{t_array[1]}'))), "
                            else:
                                mycontentstr += f"('{para_name}', '{para_oid}', SDY.PredefType(SDY.SimpleType.{para_type.upper()})), "
                        mycontentstr += "], "
                    elif pro_node.tag == "outputParameters":
                        mycontentstr += f"outputs = ["
                        parameters = pro_node.findall("./")
                        for para in parameters:
                            para_name = para.attrib.get("name")
                            para_type = para.attrib.get("type")
                            para_oid = para.attrib.get("oid")
                            if "^" in para_type:
                                t_array = para_type.split("^", 1)# type: ignore
                                mycontentstr += f"('{para_name}', '{para_oid}', SDY.ArrayType(SDY.PredefType(SDY.SimpleType.{t_array[0].upper()}), SDY.LiteralExpr('{t_array[1]}'))), "
                            else:
                                mycontentstr += f"('{para_name}', '{para_oid}', SDY.PredefType(SDY.SimpleType.{para_type.upper()})), "
                        mycontentstr += "], "
                    elif pro_node.tag == "commands":
                        mycontentstr += f"{pro_node.tag} = ["
                        commands_nodes = pro_node.findall("./")
                        # print (f"the lenth of path command is: {len(list(commands_nodes))}")
                        for command in commands_nodes:
                            if command.tag == "moveTo":
                                moveTo_x_init = get_text(command, "./startPoint/x/init")
                                moveTo_y_init = get_text(command, "./startPoint/y/init")
                                mycontentstr += f"SDY.MoveTo(start_point = ({moveTo_x_init}, {moveTo_y_init})), "
                            elif command.tag == "lineTo":
                                lineTo_x_init = get_text(command, "./endPoint/x/init")
                                lineTo_y_init = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.LineTo(end_point = ({lineTo_x_init}, {lineTo_y_init})), "
                            elif command.tag == "horizontalLineTo":
                                horizontalLineTo_endX_init = get_text(command, "./endX/init")
                                mycontentstr += f"SDY.HorizontalLineTo(end_x = {horizontalLineTo_endX_init}), "
                            elif command.tag == "verticalLineTo":
                                verticalLineTo_endY_init = get_text(command, "./endY/init")
                                mycontentstr += f"SDY.VerticalLineTo(end_y = {verticalLineTo_endY_init}), "
                            elif command.tag == "curveTo":
                                curveTo_firstx_init = get_text(command, "./firstControlPoint/x/init")
                                curveTo_firsty_init = get_text(command, "./firstControlPoint/y/init")
                                curveTo_secondx_init = get_text(command, "./secondControlPoint/x/init")
                                curveTo_secondy_init = get_text(command, "./secondControlPoint/y/init")
                                curveTo_endx_init = get_text(command, "./endPoint/x/init")
                                curveTo_endy_init = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.CurveTo(first_control_point = ({curveTo_firstx_init}, {curveTo_firsty_init}), second_control_point = ({curveTo_secondx_init}, {curveTo_secondy_init}), end_point = ({curveTo_endx_init}, {curveTo_endy_init})), "
                            elif command.tag == "smoothCurveTo":
                                curveTo_secondx_init = get_text(command, "./secondControlPoint/x/init")
                                curveTo_secondy_init = get_text(command, "./secondControlPoint/y/init")
                                curveTo_endx_init = get_text(command, "./endPoint/x/init")
                                curveTo_endy_init = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.SmoothCurveTo(second_control_point = ({curveTo_secondx_init}, {curveTo_secondy_init}), end_point = ({curveTo_endx_init}, {curveTo_endy_init})), "
                            elif command.tag == "quadraticCurveTo":
                                curveTo_controlx_init = get_text(command, "./controlPoint/x/init")
                                curveTo_controly_init = get_text(command, "./controlPoint/y/init")
                                curveTo_endx_init = get_text(command, "./endPoint/x/init")
                                curveTo_endy_init = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.QuadraticCurveTo(control_point = ({curveTo_controlx_init}, {curveTo_controly_init}), end_point = ({curveTo_endx_init}, {curveTo_endy_init})), "
                            elif command.tag == "smoothQuadraticCurveTo":
                                curveTo_endx_init = get_text(command, "./endPoint/x/init")
                                curveTo_endy_init = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.SmoothQuadraticCurveTo(end_point = ({curveTo_endx_init}, {curveTo_endy_init})), "
                            elif command.tag == "ellipticalArc":
                                xRadius = get_text(command, "./xRadius/init")
                                yRadius = get_text(command, "./yRadius/init")
                                xAxis = get_text(command, "./xAxisRotation/init")
                                ellipticalArc_largeArcFlag_init = get_text(command, "./largeArcFlag/init")
                                if ellipticalArc_largeArcFlag_init == "false":
                                    arcflag = False
                                else:
                                    arcflag = True
                                ellipticalArc_sweepFlag_init = get_text(command, "./sweepFlag/init")
                                if ellipticalArc_sweepFlag_init == "false":
                                    sweepflag = False
                                else:
                                    sweepflag = True
                                endx = get_text(command, "./endPoint/x/init")
                                endy = get_text(command, "./endPoint/y/init")
                                mycontentstr += f"SDY.EllipticalArc(x_radius = {xRadius}, y_radius = {yRadius}, x_axis_rotation = {xAxis}, large_arc_flag = {arcflag}, sweep_flag = {sweepflag}, end_point = ({endx}, {endy})), "
                            else:
                                pass
                        mycontentstr += "], "
                    elif pro_node.tag == "orientation":
                        if pro_node.attrib.get('clockwise') == "false":
                            mycontentstr += f"clockwise = False, "
                        else:
                            mycontentstr += f"clockwise = True, "
                    # elif pro_node.tag in ["lineWidth", "lineStippe"]:
                        # init = get_text(pro_node, "./init")
                        # mycontentstr += f"{attr} = {init}, "
                    elif pro_node.tag == "clipInside":
                        if top_object_name == "clipBox":
                            if pro_node.attrib.get('clipInside') == "false":
                                mycontentstr += f"clip_inside = False, "
                            else:
                                mycontentstr += f"clip_inside = True, "
                        else:
                            pass
                    elif pro_node.tag == "index":
                        if top_object_name == "hook":
                            init = get_text(pro_node, "./init")
                            mycontentstr += f"index = {init}, "
                        else:
                            pass
                    elif pro_node.tag == "lineWidth":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"line_width = {init}, "
                    elif pro_node.tag == "lineStipple":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"line_stipple = {init}, "
                    elif pro_node.tag == "replication":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"nb_instances = {init}, "
                    elif pro_node.tag == "refAngle":
                        init = get_text(pro_node, "./angle/init")
                        mycontentstr += f"ref_angle = {init}, "
                    elif pro_node.tag == "pointerId":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"pointer_id = {init}, "
                    elif pro_node.tag == "eventId":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"id = {init}, "
                    elif pro_node.tag == "input":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"input = {init}, "
                    elif pro_node.tag == "cursorId":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"id = {init}, "
                    elif pro_node.tag == "width":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"width = {init}, "
                    elif pro_node.tag == "height":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"height = {init}, "
                    elif pro_node.tag == "outlineColor":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"outline_color = {init}, "
                    elif pro_node.tag == "function":
                        init = pro_node.attrib.get("name")# type: ignore
                        mycontentstr += f"function = '{init}', "
                    elif pro_node.tag == "file":
                        init = pro_node.attrib.get("name")# type: ignore
                        mycontentstr += f"file = '{init}', "
                    elif pro_node.tag == "haloColor":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"halo_color = {init}, "
                    elif pro_node.tag == "fillColor":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"fill_color = {init}, "
                    elif pro_node.tag == "outlineOpacity":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"outline_opacity = {init}, "
                    elif pro_node.tag == "font":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"font = {init}, "
                    elif pro_node.tag == "value":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"value = {init}, "
                    elif pro_node.tag == "firstLineWidth":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"first_line_width = {init}, "
                    elif pro_node.tag == "firstFont":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"first_font = {init}, "
                    elif pro_node.tag == "secondFont":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"second_font = {init}, "
                    elif pro_node.tag == "secondLineWidth":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"second_line_width = {init}, "
                    elif pro_node.tag == "textValue":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"value = {init}, "
                    elif pro_node.tag == "textureId":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"texture_id = {init}, "
                    elif pro_node.tag == "vertAlign":   
                        init = get_text(pro_node, "./init")
                        if init == "bottom":
                            v = "VertAlignEnum.BOTTOM"
                        elif init == "middle":
                            v = "VertAlignEnum.MIDDLE"
                        elif init == "top":
                            v = "VertAlignEnum.TOP"
                        else:
                            v = "unknown in vertAlign"
                        mycontentstr += f"vert_align = SDY.{v}, "
                    elif pro_node.tag == "horizAlign":    
                        init = get_text(pro_node, "./init")
                        if init == "left":
                            v = "HorizAlignEnum.LEFT"
                        elif init == "center":
                            v = "HorizAlignEnum.CENTER"
                        elif init == "right":
                            v = "HorizAlignEnum.RIGHT"
                        else:
                            v = "unknown in horizAlign"
                        mycontentstr += f"horiz_align = SDY.{v}, "
                    elif pro_node.tag == "fillOpacity":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"fill_opacity = {init}, "
                    elif pro_node.tag == "radius":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"radius = {init}, "
                    elif pro_node.tag == "thickness":
                        init = get_text(pro_node, "./init")
                        mycontentstr += f"thickness = {init}, "
                    elif pro_node.tag == "haloing":
                        if init == "false":
                            mycontentstr += f"{pro_node.tag} = False, "
                        elif init == "true":
                            mycontentstr += f"{pro_node.tag} = True, "
                        else:
                            mycontentstr += f"{pro_node.tag} = {init}, "
                    else:
                        print (f"\n-----------{pro_node.tag} property in {top_object_name} is not deal with-----------------\n")
                mycontentstr +=")\n"
                mycontentstr = mycontentstr.replace(", )", ")")
                mycontentstr += f"{parent}.children.append({obj_name_nospace})\n" 
            elif obj_node.tag == "children" and len(list(obj_node)) > 0:
                mycontentstr += getobjectcontent(list(obj_node), obj_name_nospace)
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

out_path = "Outputs/out.py"
with open(out_path, "w") as f:
    f.write(pycode)
subprocess.call(f"python -m black {out_path}")

xmlstr = minidom.parseString(ET.tostring(nodes)).toprettyxml(
    indent="    ", encoding="utf-8"
)
with open("Outputs/out2.sgfx", "wb") as f2:
    f2.write(xmlstr)
