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


class Link:
    
    def __init__(self, oid, o_path_name, req_id):
        self.oid = oid
        self.oPathName = o_path_name
        self.reqId = req_id
