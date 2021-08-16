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


class AlmgException(Exception):
    
    def __init__(self, message, original_exception=None):

        if original_exception is None:
            super(AlmgException, self).__init__(message)
        else:
            super(AlmgException, self).__init__(message + ":" + str(original_exception))
