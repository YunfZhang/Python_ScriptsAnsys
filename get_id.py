import xml.etree.ElementTree as ET
import os
import json


def get_id(almgr_path, description):
    tree = ET.parse(almgr_path)
    root = tree.getroot()
    for traceElt in root.findall("traceableElements"):
        if description == traceElt.get("description"):
            return traceElt.get("identifier")
    return ""


# if __name__ == "__main__":
#     almgr_path = r".\Test_addelements.almgr"
#     list_child_url = [
#         "child_req",
#         "child_req2",
#         "child_req3",
#         "child_req4",
#         "child_req5",
#         "child_req6",
#         "child_req7",
#         "child_req8",
#         "child_req9",
#         "child_req10",
#         "child_req11",
#         "child_req12",
#         "child_req13",
#         "child_req14",
#         "child_req15",
#         "child_req16",
#         "child_req17",
#         "child_req18",
#         "child_req19",
#         "child_req20",
#     ]
#     for child_url in list_child_url:
#         traceEltId = get_id(almgr_path, child_url)
#         traceEltId_list = []
#         traceEltId_list.append(traceEltId)
#         print(traceEltId_list)
#     # with open ("remove_elt.json", "w"):
#     #     os.system()

#%%
URLS = [
    "https://shdvm2ws2012.win.ansys.com:9443/rm/resources/MB_5da70450dcc04cc9a6149b9d301dd38a",
    "https://shdvm2ws2012.win.ansys.com:9443/rm/resources/MB_011aa0dd94f8412da1b9b949999a13aa",
    "https://shdvm2ws2012.win.ansys.com:9443/rm/resources/MB_7aaf301627f844c5b86a590ca184a70d",
]

#%%
actions = [{"type": "REMOVE", "element": {"id": url}} for url in URLS]
json_data = {
    "doc_id": "https://shdvm2ws2012.win.ansys.com:9443/rm/resources/_Evfaca0hEemGbaLcgS1pXg",
    "actions": actions,
}

#%%
import json
from pathlib import Path
Path("toto.json").write_text(json.dumps(json_data, indent=2))


# %%
from jinja2 import Template

template_content = Path("toto.json.j2").read_text()
json_content = Template(template_content).render(urls=URLS)
Path("toto2.json").write_text(json_content)

# %%
