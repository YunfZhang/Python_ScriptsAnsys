# ===============================================================================
# Copyright (C) 2021  ANSYS, Inc. ALL RIGHTS RESERVED.
# This source file may be used and distributed without restriction provided
# that this copyright statement is not removed from the file and that any
# derivative work contains this copyright notice.
#
# Warranty
# ANSYS, Inc makes no warranty of any kind with regard to the use
# of this Software, either expressed or implied, including, but not limited to
# the fitness for a particular purpose.
# ===============================================================================

import os
import json
import pathlib
import almgateway.client as almg_client
from datetime import datetime

SCADE_HWND = "2323232"


def run_test_scenario(client, scenario_path):
    sce_cmd = []
    sce_cmd_ret = []
    test_cmd_ret = []
    with open(scenario_path, 'r') as f:
        line_kind = 1
        for line in f.readlines():
            if line_kind % 2 != 0:
                sce_cmd.append(line)
                start_time = datetime.now()
                test_cmd_ret.append(client.run(line)['value'])
                stop_time = datetime.now()
                print(f"command time: {stop_time - start_time}")
            else:
                cmd_ret = json.loads(line)['value']
                sce_cmd_ret.append(cmd_ret)
            line_kind = line_kind + 1


if __name__ == '__main__':
    almg_install_path = "C:\\Program Files\\ANSYS Inc\\v221\\0726\\SCADE LifeCycle\\ALM Gateway"
    sce_add_child_elt_path = str(pathlib.Path(".").resolve() / "./scenarios/SuiteTest_add_child_elt_sce_dng")
    sce_remove_elt_path = str(pathlib.Path(".").resolve() / "./scenarios/SuiteTest_remove_elt_sce_dng")

    almg_client.remove_workspace(os.getpid())
    client = almg_client.CommandExecutor(almg_install_path, os.getpid(), SCADE_HWND)
    print("Start ALM Gateway...")
    client.start()
    print("Execute scenarios...")
    run_test_scenario(client, sce_add_child_elt_path)
    # run_test_scenario(client, sce_remove_elt_path)
    print("Stop ALM Gateway...")
    client.stop()
