# ===============================================================================
#  (C) 2017 ESTEREL TECHNOLOGIES SAS. ALL RIGHTS RESERVED.
#  This source file may be used and distributed without restriction provided  
#  that this copyright statement is not removed from the file and that any  
#  derivative work contains this copyright notice.
# 
#  Warranty
#  ESTEREL TECHNOLOGIES SAS makes no warranty of any kind with regard to the use 
# of this Software, either expressed or implied, including, but not limited to 
# the fitness for a particular purpose.
# ===============================================================================
import os
import socket
import pathlib
import subprocess
import json
import shutil
import almgateway.exceptions as almg_exceptions

# COMMAND RETURN VALUES
# General:
ERROR = "-1"
# Settings:
RESET_CONNECTOR = "1"
# OpenProject, LoadModel, ExportStatus, addLinks, removeLinks, Export:
NOT_EXPORTED = "0"  # All ALMG information is not exported, Req file is returned
EXPORTED = "1"  # All ALMG information is exported, Req file is returned
NO_CHANGE = "2"  # Export status is not changed, Req file is not returned
# SaveProject, SaveModel, CloseProject, CloseModel, Import:
OK = "0"

# ALM GATEWAY WORKSPACE
ALMG_WORKSPACE_ROOT_PATH = pathlib.Path(os.environ['TEMP']) / "SCADE\\ALM Gateway\\workspaces"


def remove_workspace(pid):
    workspace_path = str(ALMG_WORKSPACE_ROOT_PATH / f"workspace_{pid}")
    if os.path.exists(workspace_path):
        shutil.rmtree(workspace_path)


class ScenarioExecutor:
    
    def __init__(self, almgPath, pid, hwnd):
        self.client = CommandExecutor(almgPath, pid, hwnd)
            
    def start_alm_gateway(self):
        self.client.start()
    
    def run_scenario(self, scenario_path):
        try:
            
            with open(scenario_path, 'r') as f:
                scenario = f.read()
                for cmd in scenario:
                    self.client.run(cmd)
                
        except Exception as e:
            raise almg_exceptions.AlmgException("ScenarioExecutor error", e)
        
    def stop_alm_gateway(self):
        self.client.stop()


class CommandExecutor:

    ALMG_FRONTEND_RELATIVE_PATH = ".\\bin\\scadeAlmGateway.exe"

    def __init__(self, almg_path, pid, hwnd):
        self.almgFrontendPath = str(pathlib.Path(almg_path) / CommandExecutor.ALMG_FRONTEND_RELATIVE_PATH)
        self.pid = str(pid)
        self.hwnd = hwnd
        self.client = ClientSocket()
              
    def start(self):
        try:
            cmd = [self.almgFrontendPath, "-start", self.pid, self.hwnd]
            process = subprocess.Popen(cmd)
            process.wait()
            port = process.returncode
            self.client.connect(port)
        except Exception as e:
            raise almg_exceptions.AlmgException("Start error", e)

    def run(self, command):
        try:
            return self._execute_command(command)
        except Exception as e:
            raise almg_exceptions.AlmgException("RunCommand error", e)
    
    def open_project(self, scade_project_path, req_path):
        try:
            cmd = CommandGenerator(scade_project_path, None, req_path).open_project()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("OpenProject error", e)
    
    def load_model(self, scade_project_path, scade_model_path, req_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path, req_path).load_model()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("LoadModel error", e)
    
    def settings(self, scade_project_path, scade_model_path=None):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).settings()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Settings error", e)
    
    def manage(self, scade_project_path):
        try:
            cmd = CommandGenerator(scade_project_path).manage()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Manage error", e)
        
    def migration(self, scade_project_path, rqtf_path):
        try:
            cmd = CommandGenerator(scade_project_path).migration(rqtf_path)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Migration error", e)
    
    def import_req(self, scade_project_path, scade_model_path, req_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path, req_path).import_req()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Import error", e)

    def locate(self, scade_project_path, req_id):
        try:
            cmd = CommandGenerator(scade_project_path).locate(req_id)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Locate error", e)
    
    def add_links(self, scade_project_path, scade_model_path, links):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).add_links(links)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("AddLinks error", e)
    
    def remove_links(self, scade_project_path, scade_model_path, links):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).remove_links(links)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("RemoveLinks error", e)
                   
    def export(self, scade_project_path, scade_model_path=None):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).export()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("Export error", e)
    
    def export_status(self, scade_project_path, scade_model_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).export_status()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("ExportStatus error", e)
    
    def save_project(self, scade_project_path):
        try:
            cmd = CommandGenerator(scade_project_path).save_project()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("SaveProject error", e)
    
    def save_model(self, scade_project_path, scade_model_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).save_project()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("SaveModel error", e) 
       
    def close_project(self, scade_project_path):
        try:
            cmd = CommandGenerator(scade_project_path).close_project()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("CloseProject error", e) 
           
    def close_model(self, scade_project_path, scade_model_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).close_model()
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("CloseModel error", e)
            
    def stop(self):
        try:
            cmd = CommandGenerator("No-project").stop()
            cmd_ret = self._execute_command(cmd)
            return cmd_ret
        except Exception as e:
            raise almg_exceptions.AlmgException("Stop error", e)

    def _execute_command(self, cmd):
        self.client.send(cmd)
        cmd_ret = self.client.receive().decode()
        return json.loads(cmd_ret)

    # Validation features

    def import_model(self, scade_project_path, scade_model_path, xml_model_path):
        try:
            cmd = CommandGenerator(scade_project_path, scade_model_path).import_model(xml_model_path)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("ImportModel error", e)

    def clean_document(self, scade_project_path, doc_id):
        try:
            cmd = CommandGenerator(scade_project_path, None).clean_document(doc_id)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("CleanDocument error", e)

    def modify_document(self, scade_project_path, actions_path):
        try:
            cmd = CommandGenerator(scade_project_path, None).modify_document(actions_path)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("ModifyDocument error", e)

    def remove_all_links(self, scade_project_path, doc_id):
        try:
            cmd = CommandGenerator(scade_project_path, None).remove_all_links(doc_id)
            return self._execute_command(cmd)
        except Exception as e:
            raise almg_exceptions.AlmgException("CleanDocument error", e)


class ClientSocket:
    
    RECV_MSG_LEN = 1024
    
    def __init__(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
    def connect(self, port):
        host = "localhost"
        self.sock.connect((host, port))     
    
    def send(self, msg):
        sent = self.sock.send((msg + "\n").encode())
        if sent == 0:
            raise almg_exceptions.AlmgException("The message <%s> was not sent" % msg)
    
    def receive(self):
        received = self.sock.recv(ClientSocket.RECV_MSG_LEN)
        if received == b'':
            raise almg_exceptions.AlmgException("Response is empty")
        return received
    
    def close(self):
        self.sock.close()    


class CommandGenerator:

    def __init__(self, scade_project_path, scade_model_path=None, req_path=None):
        
        self.scadeProjectPath = scade_project_path.replace("\\", "\\\\")
        
        if scade_model_path is None:
            self.scadeModelPath = None
        else:
            self.scadeModelPath = scade_model_path.replace("\\", "\\\\")
        
        if req_path is None:
            self.reqPath = None
        else:
            self.reqPath = req_path.replace("\\", "\\\\")
                
    def _check_scade_model_path(self):
        if self.scadeModelPath is None:
            raise almg_exceptions.AlmgException("scadeModelPath cannot be \'None\'")
    
    def _check_req_path(self):
        if self.reqPath is None:
            raise almg_exceptions.AlmgException("reqPath cannot be \'None\'")
    
    def open_project(self):
        
        self._check_req_path()
        
        cmd = "{"
        cmd += "\"cmd\":\"openProject\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"req_path\":\"" + self.reqPath + "\""
        cmd += "}}"
        return cmd
    
    def load_model(self):
        
        self._check_scade_model_path()
        self._check_req_path()
        
        cmd = "{" 
        cmd += "\"cmd\":\"loadmodel\"," 
        cmd += "\"arg\":{" 
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"scade_model_path\":\"" + self.scadeModelPath + "\","
        cmd += "\"req_path\":\"" + self.reqPath + "\""
        cmd += "}}"
        
        return cmd

    def _add_scade_model_path_param(self, has_next_param):
        cmd_param = ""
        if self.scadeModelPath is not None: 
            cmd_param += ", \"scade_model_path\":\"" + self.scadeModelPath + "\""
        if has_next_param:
            cmd_param = ","
        return cmd_param
    
    def settings(self):
        
        cmd = "{" 
        cmd += "\"cmd\":\"settings\","
        cmd += "\"arg\":{" 
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += self._add_scade_model_path_param(False)
        cmd += "}}"
        
        return cmd
    
    def manage(self):
        
        cmd = "{"  
        cmd += "\"cmd\":\"manage\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += "}}"
        
        return cmd
    
    def migration(self, rqtf_path):
        
        self._check_req_path()
        
        cmd = "{" 
        cmd += "\"cmd\":\"migration\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"rqtf_path\":\"" + rqtf_path + "\""
        cmd += "    }"
        cmd += "}"
        
        return cmd
         
    def import_req(self):
        
        self._check_req_path()
        
        cmd = "{" 
        cmd += "\"cmd\":\"import\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += self._add_scade_model_path_param(True)
        cmd += "\"req_path\":\"" + self.reqPath + "\""
        cmd += "}}"
        
        return cmd
    
    def locate(self, req_id):
        
        cmd = "{" 
        cmd += "\"cmd\":\"locate\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"req_id\": \"" + req_id + "\""
        cmd += "}}"
        
        return cmd
        
    def __generate_links_command(self, cmd_links, links):
           
        cmd_links_str = "{"
        cmd_links_str += "\"cmd\":\"" + cmd_links + "\","
        cmd_links_str += "\"arg\":{"
        cmd_links_str += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd_links_str += self._add_scade_model_path_param(True)
        cmd_links_str += "\"links\":["
        for link in links:
            cmd_links_str += "{"
            cmd_links_str += "\"source\":{"
            cmd_links_str += "\"oid\":\"" + link.oid + "\""
            
            if cmd_links == "addlinks":
                cmd_links_str += ", \"path_name\":\"" + link.oPathName + "\""
            
            cmd_links_str += "},"
            cmd_links_str += "\"target\":{"
            cmd_links_str += "\"req_id\":\"" + link.reqId + "\""
            cmd_links_str += "}}"
             
            if links.index(link) != len(links) - 1:
                cmd_links_str += ","
         
        cmd_links_str += "]}}"
         
        return cmd_links_str
    
    def add_links(self, links):
        return self.__generate_links_command("addlinks", links)
    
    def remove_links(self, links):
        return self.__generate_links_command("removelinks", links)
                
    def export(self):
        
        cmd = "{" 
        cmd += "\"cmd\":\"export\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += self._add_scade_model_path_param(False)
        cmd += "}}"
        
        return cmd
       
    def export_status(self):
        
        self._check_req_path()
        
        cmd = "{" 
        cmd += "\"cmd\":\"exportstatus\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"scade_model_path\":\"" + self.scadeModelPath + "\""
        cmd += "}}"
        
        return cmd
    
    def save_project(self):
        
        cmd = "{"
        cmd += "\"cmd\":\"saveproject\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += "}}"
        
        return cmd
    
    def save_model(self):
        
        cmd = "{" 
        cmd += "\"cmd\":\"savemodel\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += self._add_scade_model_path_param(False)
        cmd += "}}"
        
        return cmd

    def close_project(self):
        
        cmd = "{"  
        cmd += "\"cmd\":\"closeproject\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += "}}"
    
        return cmd
    
    def close_model(self):
        
        self._check_scade_model_path()
        
        cmd = "{" 
        cmd += "\"cmd\":\"closemodel\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"scade_model_path\":\"" + self.scadeModelPath + "\""
        cmd += "}}"
        
        return cmd
    
    def stop(self):
        return "{\"cmd\":\"stop\"}"

    def import_model(self, xml_model_path):

        cmd = "{"
        cmd += "\"cmd\":\"importmodel\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\""
        cmd += self._add_scade_model_path_param(True)
        cmd += "\"import_model_path\":\"" + xml_model_path + "\""
        cmd += "}}"

        return cmd

    def clean_document(self, doc_id):

        cmd = "{"
        cmd += "\"cmd\":\"cleandocument\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"doc_id\":\"" + doc_id + "\""
        cmd += "}}"

        return cmd

    def modify_document(self, actions_path):

        cmd = "{"
        cmd += "\"cmd\":\"cleandocument\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"actions_path\":\"" + actions_path + "\""
        cmd += "}}"

        return cmd

    def remove_all_links(self, doc_id):

        cmd = "{"
        cmd += "\"cmd\":\"removealllinks\","
        cmd += "\"arg\":{"
        cmd += "\"scade_project_path\":\"" + self.scadeProjectPath + "\","
        cmd += "\"doc_id\":\"" + doc_id + "\""
        cmd += "}}"

        return cmd
