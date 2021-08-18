import re
import glob
import subprocess
import xml.etree.ElementTree as ET
from xml.dom import minidom
from typing import List, Dict, Any

in_path = "UADF.sgfx"
tree = ET.parse(in_path)
nodes = tree.getroot()

# added imported
pycode = "import os\n"
pycode += "import scade.model.a661 as UAPC\n\n\n"




# added layer
layer_node = nodes.find("./children/A661Layer")
layer_oid = layer_node.get("oid")  # type: ignore #(all layer has <oid>)
layer_name = layer_node.get("name")  # type: ignore #(all layer has <oid>)
pycode += f'A661Layer = UAPC.LayerInstance(name = "{layer_name}", oid = "{layer_oid}", width = 15360, height = 15360, children=['


widget_str = ""

scalar_prop_dict = {'intprop':"IntPropValue",'floatprop':"FloatPropValue",'stringprop':"StringPropValue"}

def get_props(w_props, str_log) -> str:
    temp_str = ""
    for prop in w_props:
        prop_name = prop.get("name")
        prop_value = prop.text
        if str_log == "rootprop":
            temp_str += 'UAPC.DefinitionAttribute('
            temp_str += f'name = "{prop_name}", '
        else:
            pass
        if prop.tag in scalar_prop_dict:
            if prop.tag == "stringprop":
                prop_value = prop_value.replace('\"','&quot;').replace('\'','&apos;')
            else:
                pass
            if str_log == "rootprop":
                temp_str += f'value = UAPC.{scalar_prop_dict.get(prop.tag)}(value="{prop_value}")'
            else:
                temp_str += f'UAPC.{scalar_prop_dict.get(prop.tag)}(value="{prop_value}"), '
        elif prop.tag == "arrayprop":
            temp_str += f'value = UAPC.ArrayPropValue(['
            arrayprops = prop.findall("./")
            temp_array= get_props(arrayprops, "subprop")
            temp_str += temp_array
            temp_str += '])'
        elif prop.tag == "structprop":
                temp_str += f'UAPC.StructPropValue(['
                structprops = prop.findall("./")
                temp_struct = get_props(structprops,"rootprop")
                temp_str += temp_struct
                temp_str += ']),'
        elif prop.tag == "enumprop":
            if str_log == "rootprop":
                temp_str += f'value = UAPC.EnumPropValue(value=UAPC.A661Constant(name="{prop_value}"))'
            else:
                temp_str += f'UAPC.EnumPropValue(value=UAPC.A661Constant(name="{prop_value}")),'
        else:
            print (f"----unknown prop: {prop.tag} detected---")
        if str_log == "rootprop":
            temp_str += '),'
        else:
            pass
    return temp_str


def getobjectcontent(widgets_nodes: List[ET.Element], parent = "") -> str:
    """Return string corresponding to objects"""
    mycontentstr = ""
    for widgets in widgets_nodes:
        widget_oid = widgets.get("oid")
        widget_name = widgets.get("name")
        widget_type = widgets.get("type")
        if parent != "":
            mycontentstr += f'UAPC.WidgetInstance('
        else:
            mycontentstr += 'UAPC.WidgetInstance('
        #start to add props under model
        mycontentstr += f'name = "{widget_name}", oid = "{widget_oid}", type = UAPC.A661Widget(name="{widget_type}"), props = ['
        widget_props = widgets.findall("./model/")
        mycontentstr += get_props(widget_props, "rootprop") 
        mycontentstr += '], ' #match props loop: props = [***
        
        #start to add runtime
        widget_runtime = widgets.findall("./runtime/")
        if len(widget_runtime) != 0:
            mycontentstr += "runtime_messages= ["
            for r in widget_runtime:
                msg_id = r.get("msg_id")
                name = r.get("name")
                mycontentstr += f'UAPC.ConnectedMessage(id="{msg_id}", name="{name}"), '
            mycontentstr += "], "
        else:
            mycontentstr += "runtime_messages= None, "
        
        # #start to add event
        widget_event = widgets.findall("./events/")
        if len(widget_event) != 0:
            mycontentstr += "events= ["
            for e in widget_event:
                msg_id = e.get("msg_id")
                name = e.get("name")
                mycontentstr += f'UAPC.ConnectedMessage(id="{msg_id}", name="{name}"), '
            mycontentstr += "], "
        else:
            mycontentstr += "events= None, "

        # #start to add children 
        widget_children = widgets.findall("./children/")
        if len(widget_children) != 0:
            mycontentstr += "children= ["
            mycontentstr += getobjectcontent(widget_children, "")
            mycontentstr += "], "
        else:
            mycontentstr += "children = None, "

        mycontentstr += '), \n'#match UAPC.WidgetInstance(
    return mycontentstr



#start to get widget content
widget_nodes = nodes.findall("children/A661Layer/children/")
# for objects in object_nodes:
widget_str = getobjectcontent(widget_nodes, "A661Layer")




pycode += widget_str
pycode += '], ) \n'  #match UAPC.LayerInstance(

pycode += "model = UAPC.DefinitionFile(width = 768, height = 768, ratio = (20, 20), layers = [A661Layer])\n\n\n"
# save the Specification to a given location
pycode += "output_path = 'Outputs/out_uapc_1.sgfx'\n"
pycode += "os.makedirs(os.path.dirname(output_path), exist_ok=True)\n"
pycode += "UAPC.save_sgfx(model, output_path)\n"

out_path = "Outputs/out.py"
with open(out_path, "w") as f:
    f.write(pycode)
subprocess.call(f"python -m black {out_path}")