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

SDY_Installation = "C:/ANSYS/v211/TED_0709"

start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED"
# start_folder = "C:/AnsysDev/TE-DISPLAY-2021/TCP_TED/Test_Data/Batch_TED/TE_SequenceFiles"
# start_folder = "C:/AnsysDev/SDY_IDE/Workdir_SDYIDE/test/I_Circle"

log_files=[]

log_files = Path(start_folder).rglob('*.log')

for log_file in log_files:
    log_file = str(log_file).replace("\\","/")
    print (log_file)
    if "SDYTEE_Batch" in log_file:
        new_log_file = log_file.replace("SDYTEE_Batch.log", "QTETEE_SDY_Batch.log")
        cmd = f'svn rename "{log_file}" "{new_log_file}"'
        print (f"SDYTEE cmd is: {cmd}")
        subprocess.call(cmd)
    elif "SDYTTE_Batch" in log_file:
        new_log_file = log_file.replace("SDYTTE_Batch.log", "QTETHG_SDY_Batch.log")
        cmd = f'svn rename "{log_file}" "{new_log_file}"'
        print (f"SDYTTE cmd is: {cmd}")
        subprocess.call(cmd)
    else:
        pass