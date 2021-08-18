import os
import shutil
import re
import glob

#the script is used to copy bmp file from "Images_ref" folder to "Images_chk" folder
#meanwhile, it will changed bmp name from "chk_01.bmp" to "ref_01.bmp"

start_folder = "E:/svn/SDY_r20/TCP_TEST/TCP_TED/Test_Data/Batch_TED"
# start_folder = "E:/svn/SDY_r20/TCP_TEST/TCP_TED/Test_Data/Batch_TED/TE_InputFiles/SDY_Objects/C_RotationFilter/Inputs/TED_C_RotationFilter"
# list_Images_ref = [d[0].replace('\\','/') for d in os.walk(f"{start_folder}") if re.search(r'Images_ref$', d[0])]
list_Images_files = [f.replace('\\','/') for d in os.walk(f"{start_folder}") if re.search(r'Images_ref$', d[0]) for f in glob.glob(os.path.join(d[0], "*.bmp"))]
for bmp in list_Images_files:
    src = bmp.replace("Images_ref", "Images_chk").replace("ref_", "chk_")
    if os.path.isfile(src):
        shutil.copy(src, bmp)
