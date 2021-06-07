import unittest
from resource import base
from resource import testCase
from resource import avs_Login
import os


 
class Android_LIBRE_MAVID_APP_POST_AVS_FAIL(unittest.TestCase):
    "Class to run tests against the Mavid App "
    
    #Start the appium server programatically
    base.start_appium_server()
    
    #initializing the Driver
    driver = base.setUp()
    base.start_screen_record(driver,logger)
    try:
        driver.implicitly_wait(30)
        time.sleep(10)
        testCase.verify_avs_login_on_post_setup(driver)
    except Exception:
        #Kill the Driver
        base.tearDown(driver)
    
        #stop the appium server programatically
        base.stop_appium_server()
        time.sleep(5)
        os.system("start /B start cmd.exe @cmd /k"+base.working_dri()+"py post_avs_fail.py")
       
        
    
    #Kill the Driver
    base.tearDown(driver)
    
    #stop the appium server programatically
    base.stop_appium_server()
        
 

        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_LIBRE_MAVID_APP_POST_AVS_FAIL)
    unittest.TextTestRunner(verbosity=2).run(suite)