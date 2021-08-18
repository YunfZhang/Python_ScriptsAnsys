#####################################################
#USAGE:
#The script is used to send message to UA
#by change the values in send_block
#note: the script should put under PythonLib folder

#####################################################
#####################################################

from a661test import TestFramework
from a661libgen_rev6_v1 import *
from src.a661libstd import UA
from time import sleep

Standard_rev6_v1()
te=TestFramework()
ua = UA(1)
ua.connect()

#########start to send message#######################
ua.send_block([GpRectangle(2).visible(False)])
sleep(1)
ua.send_block([GpRectangle(2).visible(True)])
sleep(1)
ua.send_block([GpRectangle(2).pos_x(6000)])
sleep(1)
ua.send_block([GpRectangle(2).pos_y(6000)])
sleep(1)
ua.send_block([GpRectangle(2).style_set(12).pos_x(1000)])
sleep(1)
ua.send_block([GpRectangle(2).style_set(10), CheckButton(1).visible(False)])
sleep(1)
ua.send_block([CheckButton(1).visible(True).style_set(220)])
sleep(1)