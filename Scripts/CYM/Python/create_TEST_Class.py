import os
import re
from glob import glob
import subprocess
import shutil
import xml.etree.ElementTree as ET
from xml.dom import minidom

#the script use class -> just translate the create_TEST.py into class format.

#Load Test Environment
try: 
    import ENVIRONMENT as ENV
except Exception as e: 
    print ("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
    raise Exception

def prettify(elem):
    '''Print result of a XML tree in a pretty way'''
    reparsed = minidom.parseString(ET.tostring(elem, 'utf-8'))
    return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])

class NEWSTART(object):
    def __init__(self, path: str) -> None:
        self.list_test_etp = list() # type: List[str]
        self.list_sgfx_ogfx = list() # type: List[str]
        self.path = path
        print ("this is in initial function")

    def migrate_sgfx(self):
        self.list_sgfx_ogfx = [f.replace('\\','/') for f in glob(f"{self.path}/Inputs/*.[so]gfx")]
        for files in self.list_sgfx_ogfx:
            print (f"this is in {files}")
        pass
    def create_TEST(self):
        print ("this is in create_TEST")
        pass
    def run_cmd(self):
        print ("this is in run_cmd")
        pass

list_html = [f.replace('\\','/') for d in os.walk(".") for f in glob(os.path.join(d[0], '*TC_N*.htm*'))]
list_folder = list()
for html in list_html:
    html_folder, html_name = os.path.split(html)
    list_folder.append(html_folder)

for folder in set(list_folder):
    print (folder)
    project = NEWSTART(folder)
    project.migrate_sgfx()
    project.create_TEST()
    project.run_cmd()
