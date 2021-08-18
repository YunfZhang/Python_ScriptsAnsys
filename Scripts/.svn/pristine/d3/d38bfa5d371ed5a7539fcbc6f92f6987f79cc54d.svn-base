#!/python
#
# Date: 2 November 2016
# Author: Jean-Francois THUONG
# Purpose: Change IDs of TCP of SDY Batch Mode
#           

#Print function (3.x style)
from __future__ import print_function
try: import future
except Exception as e: print("\nNote: You can install 'future' module with 'pip install future'")

from glob import glob
import os
import re
from shutil import rmtree
import subprocess
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

class TestCase(object):
	def __init__(self, id, path):
		self.id = id
		self.path = path
		self.dir = re.sub(r'/\w+\.html', '', path)

#List Test Cases
list_TestCases = dict()
list_html = [d.replace('\\','/') for d in glob("*/*/*.html")]
for path in list_html:
	id = re.sub(r'.*\W(\w+_\d+)\.\w+', r'\1', path)
	try: list_TestCases[id] = TestCase(id=id, path=path)
	except Exception as e: print("Error in path '{path}: {e}".format(path=path, e=e))

for tc in sorted(list_TestCases.values(), key=lambda t:t.id):
#Get new TC ID
	tc.newid = re.sub(r'SDY_[A-Z]+', 'SDY_BATCH', tc.id)
	if 'CHECKTXT' in tc.id:
		tc.newid = re.sub(r'(\d+)', lambda m: '{:03d}'.format(int(m.group(1))+24), tc.newid)
	else: pass
	tc.newpath = tc.path.replace(tc.id, tc.newid)
	
#Rename files and folders
	subprocess.call("svn move {0.path} {0.newpath}".format(tc))
	subprocess.call("svn move {0.dir}/expected_results/{0.id} {0.dir}/expected_results/{0.newid}".format(tc))
	
#Update TC description	
	with open(tc.newpath, 'r') as f:
		content = f.read()
		
	content = content.replace(tc.id, tc.newid)
	
	with open(tc.newpath, 'w') as f:
		f.write(content)
	
#########
#- END -#
#########
