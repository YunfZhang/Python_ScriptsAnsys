#!python
import os
import shutil

#load test environment
try: 
    import ENVIRONMENT as ENV
except Exception as e:
    print ("Test Environment not set in 'ENVIRONMENT.py'.\nYou can use template 'ENVIRONMENT_Template.py' to do so!")
    raise

#Get the installation path and initial directory of API
api_dir = os.path.join(ENV.SCADE_DIR, "SCADE/APIs/Python/lib")

# delete the existing 'scade' path
if os.path.exists("./scade"):
    shutil.rmtree("./scade")
else:
    pass
# copy the Python API from installation to current path
dst="./scade"
shutil.copytree(api_dir + '/scade', dst)