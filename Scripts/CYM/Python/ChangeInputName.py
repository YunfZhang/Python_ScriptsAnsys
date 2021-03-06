import xml.etree.ElementTree as ET
from xml.dom import minidom
import re

###################### Configuration management information : ################# 
# Last updater:		$Author: yimchen $
# Date:				$Date: 2018-02-07 17:21:57 +0800 (周三, 07 2月 2018) $
# Revision:			$Revision: 18659 $
###############################################################################

###############################################################################
#the script is to update variable name in xscade file
#1. copy variables from sgfx
#2. paste variables into log file with this format "varname\tint"
#3. create variables in suite with default name
#4. updated int(id) condition for different types
###############################################################################


var_list = list()

with open("namelist2.log","r") as f:
    var_list = f.readlines()
    
var_list = [v.strip() for v in var_list]
int_list = [v.split("\t")[0] for v in var_list if "int" in v]
real_list = [v.split("\t")[0] for v in var_list if "real" in v]
bool_list = [v.split("\t")[0] for v in var_list if "bool" in v]
char_list = [v.split("\t")[0] for v in var_list if "char" in v]

print ("int list is: {}, real list is: {}, bool list is: {}, char list is: {}".format(len(int_list), len(real_list), len(bool_list), len(char_list)))

initial_xscade = "Operator1.xscade"
# initial_xscade = "Operator1_Simple.xscade"
content_list = list()
with open (initial_xscade, 'r') as f:
    content_list=f.readlines()

output_str = ""
for line in content_list:
    if 'Variable name="Input' in line:
        id = re.search(r'Variable name="Input(\d+)"', line).group(1)
        if int(id) <= 1071:
            a = int_list[0]
            line = re.sub(r'Variable name="\w+"', r'Variable name="%s"'%a, line)
            del int_list[0]
        elif int(id) > 1071 and int(id) <= 2124:
            a = real_list[0]
            line = re.sub(r'Variable name="\w+"', r'Variable name="%s"'%a, line)
            del real_list[0]
        elif int(id) > 2124 and int(id) <= 2159:
            a = char_list[0]
            line = re.sub(r'Variable name="\w+"', r'Variable name="%s"'%a, line)
            del char_list[0]
        else:
            a = bool_list[0]
            line = re.sub(r'Variable name="\w+"', r'Variable name="%s"'%a, line)
            del bool_list[0]
    output_str += line

with open("a_out.xscade","w") as f:
    f.write(output_str)