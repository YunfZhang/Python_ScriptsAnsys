import re
import os
from glob import glob


def get_projects(start_folder):
    suite_projects = list()
    etp_lists = (f.replace("\\", "/") for d in os.walk(start_folder) for f in glob(os.path.join(d[0], "*.etp")))
    for etp in etp_lists:
        folder = os.path.split(etp)[0]
        xscade_files = [f1.replace("\\", "/") for f1 in glob(f"{folder}/*.xscade")]
        sdy_files = [f1.replace("\\", "/") for f1 in glob(f"{folder}/*.sdy")]
        if len(xscade_files):
            suite_projects.append(etp)
            for xscade_file in xscade_files:
                suite_projects.append(xscade_file)
        if len(sdy_files) > 0:
            for sdy_file in sdy_files:
                suite_projects.append(sdy_file)
    return suite_projects


def file_modifier(file_in, file_out=None):
    '''Filter files to compare them

    Args:
        file_in(str): path of input file
        file_in(str): path of output file (default: file_in)
    '''
    if file_out is None: file_out = file_in
    with open(file_in,'r') as f:
        content = f.read()
    #Log file
    if '.etp' in file_in:
        patterns = [
            (r'<value>SCADE64</value>', r'<value>SCADE65</value>'),
            (r'<value>C QUAL64</value>', r'<value>C QUAL65</value>'),
            (r'libraries\\(lib\w+\\\w+\.etp)', r'libraries\\SC65\\\1'),
        ]
    elif '.xscade' in file_in:
        patterns = [
            (r'(xmlns=".*/ns/scade)/\d"', r'\1/6"'),
            (r'(xmlns=".*/ns/scade/pragmas/editor)/\d"', r'\1/6"'),
            (r'(xmlns:ed==".*/ns/scade/pragmas/editor)/\d"', r'\1/6"'),
            (r'(<TypeRef name=")real("/>)', r'\1float32\2'),
            (r'(<TypeRef name=")int("/>)', r'\1int32\2'),
        ]
    elif '.sdy' in file_in:
        patterns = [
            (r'(Variable name=.*)type="int"', r'\1type="int32"'),
            (r'(Variable name=.*)type="real"', r'\1type="float32"'),
        ]
    else:
        raise Exception('Incorrect type of file to filter: {}'.format(file_in))
    #Filter
    for patt_src, patt_dest in patterns:
        try:
            content = re.sub(patt_src, patt_dest, content, flags=re.M)
        except Exception as e: print("{} - {} => {}".format(patt_src, patt_dest, e))
    #Write in output file
    with open(file_out, 'w') as f_o:
        f_o.write(content)

if __name__ == "__main__":
    start_folder = "C:/AnsysDev/T2020/TCP_WL/TCP_SDY_WL"
    for f in get_projects(start_folder):
        file_modifier(f)
