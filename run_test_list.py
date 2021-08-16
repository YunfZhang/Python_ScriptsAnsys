import time
import unittest
from TestCases import *

# class testSelection()
def test_suite():
    # Select test cases by one of those choices (uncomment the selected one):
    # 1. select list of test cases from variable test_case_list
    # The following variable contains the list of test cases to be executed:
    test_case_list = [
        # "TestCases.Export_Performance.TC_SLC_ALM_SC_DNG_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_SC_Jama_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_SC_Polarion_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_SCA_DNG_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_SCA_Jama_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_SCA_Polarion_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_TE_DNG_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_TE_Jama_02_01",
        # "TestCases.Export_Performance.TC_SLC_ALM_TE_Polarion_02_01",
        # "TestCases.Export_Performance.parallel.TC_SLC_ALM_SC_DNG_02_02",
        # "TestCases.Export_Performance.parallel.TC_SLC_ALM_SC_DNG_02_03",
        # "TestCases.Import_Performance.TC_SLC_ALM_SC_Native_01_01.py",
        # "TestCases.Import_Performance.TC_SLC_ALM_SC_Native_01_02.py",
        # "TestCases.Import_Performance.TC_SLC_ALM_SC_Polarion_01_01.py",
        "TestCases.Import_Performance.TC_SLC_ALM_SCA_DNG_01_01.py",
    ]
    
    test_suites = [unittest.defaultTestLoader.loadTestsFromName(TC) for TC in test_case_list]
    test_suite = unittest.TestSuite(test_suites)
    

    return test_suite


if __name__ == '__main__':

    suite = test_suite()
    start_time=time.ctime()
    unittest.TextTestRunner(verbosity=2).run(suite)