#!/python
#
# Date: 1 November 2016
# Author: Jean-Francois THUONG
# Purpose: re-organizing some test cases description and inputs/outputs
#          Previously: 
#           * all the html files were in a sub-folders checkCSV and checkTXT
#           * input files were in folder TCP_Editor/Models/Checker_Models
#           * expected results were in a common folder expected_results in each sub-folder
#
#          The idea is to organize based on the name of models with 1 folder per TC
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
list_html = [d.replace('\\','/') for d in glob("*/*.html")]
for path in list_html:
	id = re.sub(r'.*\W(\w+_\d+)\.\w+', r'\1', path)
	try: list_TestCases[id] = TestCase(id=id, path=path)
	except Exception as e: print("Error in path '{path}: {e}".format(path=path, e=e))

for tc in sorted(list_TestCases.values(), key=lambda t:t.id):
#Get basename and update path
	with open(tc.path, 'r') as f:
		content = f.read()
	try: tc.basename = re.search(r'(\w+)\.etp', content).group(1)
	except AttributeError as e: print("Error in TC {0.id}: {1}".format(tc, e))
	
	content = content.replace('../Models', '../../Models')
	content = re.sub(r'<a href="./">.*</a>', '<a href="./">{0.dir}/{0.basename}</a>'.format(tc), content)
	
	with open(tc.path, 'w') as f:
		f.write(content)
	
#Create new folder and SVN move
	tc.new_dir = "{0.dir}/{0.basename}".format(tc)
	if os.path.exists(tc.new_dir):
		rmtree(tc.new_dir)
	os.mkdir(tc.new_dir)
	subprocess.call("svn add {0.new_dir}".format(tc))
	subprocess.call("svn move {0.path} {0.new_dir}".format(tc))
	
#Folder for expected results
	tc.exp_dir = "{0.new_dir}/expected_results".format(tc)
	if not os.path.exists(tc.exp_dir): 
		os.mkdir(tc.exp_dir)
	subprocess.call("svn add {0.exp_dir}".format(tc))
	subprocess.call("svn move {0.dir}/expected_results/{0.id} {0.exp_dir}".format(tc))
	
#Copy input
	tc.input_dir = "{0.new_dir}/input".format(tc)
	if not os.path.exists(tc.input_dir): 
		os.mkdir(tc.input_dir)
	subprocess.call("svn add {0.input_dir}".format(tc))
	subprocess.call("svn copy ../../Models/Checker_Models/{0.basename}/*.* {0.input_dir}".format(tc))
	