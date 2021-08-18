import os
import re
from glob import glob
import subprocess
import shutil
import xml.etree.ElementTree as ET
from xml.dom import minidom


#1. the script is used to migrate sgfx/ogfx file into a project
#2. then create a test project -> but actually, just copy an example test project and modify it
#3. run command cmd_sdymcins
#4. run command cmd_sdytee
#5. run command cmd_sdymcreport

#Load Test Environment
try: 
    import ENVIRONMENT as ENV
except Exception as e: 
    print ("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
    raise Exception

class CREATE_TEST(object):
    def __init__(self):
        pass

def prettify(elem):
    '''Print result of a XML tree in a pretty way'''
    reparsed = minidom.parseString(ET.tostring(elem, 'utf-8'))
    return '\n'.join([line for line in reparsed.toprettyxml(indent=' '*2).split('\n') if line.strip()])


#to modify file content, replace SDY_Example or specification.sgfx to given name
def modify_file_content(file, etp):
    content = ""
    if os.path.isfile(file):
        with open(file,'r') as f1:
            for line in f1:
                if re.search(r'SDY_Example', line):
                    line = re.sub(r'SDY_Example', '{}'.format(etp), line)
                if re.search(r'specification.sgfx', line):
                    line = re.sub(r'specification\.sgfx', '{}.sgfx'.format(etp), line)
                content += line
        with open(file, 'w') as f2:
            f2.write(content)

#to add stp file in etp
def add_stp(source_file, stp_files):
    tree = ET.parse(source_file)
    root = tree.getroot()
    FileRef_stp = root.findall('./roots/')
    for stp in FileRef_stp:
        if stp.get('extensions') == "stp":
            id = int(stp[0][0].get('id'))
            stp[0].remove(stp[0][0])
            for stpfile in stp_files:
                node = ET.Element('FileRef')
                node.set('id',str(id))
                node.set('persistAs',stpfile)
                id += 1
                stp[0].append(node)
        else:
            pass
    with open(source_file,"w") as f:
        f.write(prettify(root))

#Folders of Test Cases and Procedures Repository
dir_TP = os.path.dirname(os.path.abspath(__file__))

# start_path = "E:/svn/scade-6-7/TOR_TCP/Test_Data/SDYKCG_TORSTRAT_CMD_08/Combi_Options"
start_path = "E:/svn/scade-6-7"
if not os.path.isdir(start_path):
    print (f"Error: cannot find {start_path}, please correct it.")
    exit()
# start_path = dir_TP

#List norminal Test Cases
os.chdir(start_path)
# list_TestCases = dict()
list_html = [f.replace('\\','/') for d in os.walk(".") for f in glob(os.path.join(d[0], '*TC_N*.htm*'))]

#remove the existed SDY_*** folder and TEST_*** folder under Inputs folder
for html in list_html:
    html_folder, html_basename = os.path.split(html)
    etp_name = re.sub(r'.*\/(\w+)', r'\1',html_folder)
    SDY_etp_folder = f"{html_folder}/Inputs/SDY_{etp_name}"
    TEST_etp_folder = f"{html_folder}/Inputs/TEST_{etp_name}"
    if os.path.exists(SDY_etp_folder):
        shutil.rmtree(SDY_etp_folder)
    else:
        pass
    if os.path.exists(TEST_etp_folder):
        shutil.rmtree(TEST_etp_folder)
    else:
        pass

#start code
for html in list_html:
    html_folder, html_basename = os.path.split(html)
    source_file_list = glob(f"{html_folder}/Inputs/*.[so]gfx")
    sgfx_files = glob(f"{html_folder}/Inputs/*.sgfx")
    etp_name = re.sub(r'.*\/(\w+)', r'\1',html_folder)
    SDY_etp_folder = f"{html_folder}/Inputs/SDY_{etp_name}"
    TEST_etp_folder = f"{html_folder}/Inputs/TEST_{etp_name}"
    #create SDY_folder and SDY project
    if not os.path.exists(SDY_etp_folder):
        os.mkdir(SDY_etp_folder)
        for source_file in source_file_list:
            shutil.copy(source_file, f"{SDY_etp_folder}")
            cmd = f"{ENV.SDY_ConsoleBin} batch migrate {source_file} -project {SDY_etp_folder}/SDY_{etp_name}.etp"
            subprocess.call(cmd)
    else:
        pass
    #create TEST_folder and TEST project
    etp_full_path = f"{TEST_etp_folder}/TEST_{etp_name}.etp"
    if not os.path.exists(TEST_etp_folder):
        os.mkdir(TEST_etp_folder)
        #copy etp file
        shutil.copy(f"{dir_TP}/TEST_Example/TEST_Example.etp", f"{etp_full_path}")
        #modify the sdy etp name in the test etp
        modify_file_content(etp_full_path, f"SDY_{etp_name}")
        i=1
        for sgfx in sgfx_files:
            sgfx_name = re.sub(r'\\',r'/',sgfx)
            sgfx_name = re.sub(r'.*/(\w+)\.sgfx', r'\1', sgfx_name)
            #copy stp file
            shutil.copy(f"{dir_TP}/TEST_Example/Procedure1.stp", f"{TEST_etp_folder}/Procedure{i}.stp")
            #replace the specification in stp file
            modify_file_content(f"{TEST_etp_folder}/Procedure{i}.stp", sgfx_name)
            i += 1
        #copy sss file
        shutil.copy(f"{dir_TP}/TEST_Example/Scenario1.sss", f"{TEST_etp_folder}/Scenario1.sss")
        #list all stp files under TEST_*** folder
        stp_files = [re.sub(r'.*\\(\w+\.stp)', r'\1',f) for f in glob(f"{TEST_etp_folder}/*.stp")]
        if len(stp_files) > 1:
            #update the stp in etp file
            add_stp(etp_full_path, stp_files)
        else:
            pass
        
    else:
        pass

list_test_etp = [f.replace('\\','/') for d in os.walk(".") for f in glob(os.path.join(d[0], 'TEST_*.etp'))]
log_file = f"{dir_TP}/log_file.log"
if os.path.exists(log_file):
    os.remove(log_file)

for test_etp in list_test_etp:
    sdy_etp = test_etp.replace("TEST_", "SDY_")
    TEST_etp_folder, TEST_etp_name = os.path.split(test_etp)
    #SDYMCINS command line
    cmd_sdymcins = f"{ENV.SDYMCINS_ConsoleBin} {sdy_etp} -conf Simulation -criterion DC"
    print (f"\n-------start execute command line: {cmd_sdymcins}--------\n")
    cmd_sdymcins_status = subprocess.call(cmd_sdymcins)
    print (f"\n-------end of execute command line: {cmd_sdymcins} --------\n")
    stp_files = [f.replace('\\','/') for f in glob(f"{TEST_etp_folder}/*.stp")]
    for stp in stp_files:
        stp_folder, stp_name = os.path.split(stp)
        target_dir = f"{stp_folder}/TEST_SDYMC" + re.sub(r'.*\w+(\d).stp',r'\1',stp)
        cov_files = re.sub(r'.*\/(\w+)\.stp',r'\1',stp) + ".dmp"
        cmd_sdytee = f"{ENV.TED_ConsoleBin} {sdy_etp} -conf Simulation -nogen -test_file {stp} -target_dir {target_dir}"
        print (f"\n-------start execute command line: {cmd_sdytee}--------\n")
        cmd_sdytee_status = subprocess.call(cmd_sdytee)
        print (f"\n-------end of execute command line: {cmd_sdytee}--------\n")
        cmd_sdymcreport = f"{ENV.SDYMCREPORT_ConsoleBin} {sdy_etp} -conf Simulation -cov_files {target_dir}/{cov_files} -target_dir {target_dir}"
        print (f"\n-------start execute command line: {cmd_sdymcreport}--------\n")
        cmd_sdymcreport_status = subprocess.call(cmd_sdymcreport)
        print (f"\n-------end of execute command line: {cmd_sdymcreport}--------\n")
        info_pass = f"Passed ===> {test_etp} on {stp_name}\n"
        info_failed = f"Failed  ===> {test_etp} on {stp_name}\n"
        if (cmd_sdymcins_status == cmd_sdymcreport_status) and  (cmd_sdymcreport_status == cmd_sdytee_status):
            with open(log_file, 'a') as f:
                f.write(info_pass) 
        else:
            with open(log_file, 'a') as f:
                f.write(info_failed) 
