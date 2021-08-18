#!python

#the script used to add below command into tc
#<div class="cmd">
# <code>SDYKCG -texturemax 1024 -map
# -outdir {output}_Code color_table.sct line_width_table.swt line_stipple_table.sst texture_table.stt font_table.sft {sgfx_file}</code></div>\n'
import os
import sys
import re
from pathlib import Path, PurePath
import shutil
# from glob import glob
from textwrap import dedent
from bs4 import BeautifulSoup
import subprocess
import pprint
from lxml import etree, html

SDY_Installation = "C:/ANSYS/v211/TED_0709"

# start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED"
start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED/TE_SequenceFiles"
# start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED/TE_InputFiles/SDY_Types"
# start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED/TE_InputFiles/SDY_Objects/C_Group"
# start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED/TE_InputFiles/SDY_Objects/C_Panel"

html_tc_path=[]

# for d in os.walk("%s" % start_folder):
#     for f in glob(os.path.join(d[0], 'TEST_TED_*.htm')):
#         html_tc_path.append("%s" % f.replace("\\","/"))

html_tc_path = Path(start_folder).rglob('TEST_TED_*.htm')
# print (html_tc_path)

def get_stp(html_file):
    with open(html_file,'r') as f:
        content = f.read()
    soup = BeautifulSoup(content,'lxml')
    for href in soup.find_all("a"):
        # print(href)
        stp_text = href.get_text()
        if ".stp" in stp_text:
            return stp_text
    # print (soup)
    return "NOT FOUND"

def get_sgfx_from_stp(stp_file):
    with Path(stp_file).open() as f:
        content = f.read()
    soup = BeautifulSoup(content,'xml')
    sgfx_file = soup.Procedure['operator']
    return sgfx_file

def set_command_line(sgfx_file):
    if ".sgfx" in sgfx_file:
        output = sgfx_file.replace(".sgfx","")
    else:
        output = sgfx_file.replace(".ogfx","")
    cmd = f'  <div class="cmd"><code>SDYKCG -texturemax 1024 -map -outdir {output}_Code color_table.sct line_width_table.swt line_stipple_table.sst texture_table.stt font_table.sft {sgfx_file}</code></div>\n'
    return cmd

def insert_html_file(cmd, html_file):
    new_content = ""
    with Path(html_file).open() as f:
        content = f.readlines()
    for line in content:
        if "4.Command Line" in line:
            line += cmd
            new_content += line
        else:
            new_content += line
    with Path(html_file).open(mode="w") as f:
        f.write(new_content)


for html_tc in html_tc_path:
    print(f"\n\n----> start to deal with {html_tc}")
    html_path = PurePath(html_tc).parent
    html_name = PurePath(html_tc).name
    stp_file = get_stp(html_tc)
    if stp_file == "NOT FOUND":
        pass
    else:
        sgfx_file = get_sgfx_from_stp(f"{html_path}/{stp_file}")
        codegen_cmd=set_command_line(sgfx_file)
        # print (codegen_cmd)
        insert_html_file(codegen_cmd, html_tc)
