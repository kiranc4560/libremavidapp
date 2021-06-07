import unittest
from selenium.webdriver.common.by import By
from resource.data import data
from resource import testCase
from resource import avs_Login
from datetime import datetime
from resource import base
import logging
import time
import os


 
class Android_LIBRE_MAVID_APP(unittest.TestCase):
    "Class to run tests against the Mavid App "
    #Create and configure logger
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename=os.path.join(base.working_dri()+"\logs" ,"mavidApp_Automation_logs"+tm+".log"),
                    format='%(asctime)s %(message)s',
                    filemode='a')
    
    #Creating an object
    logger=logging.getLogger()
  
    #Setting the threshold of logger to DEBUG
    logger.setLevel(logging.INFO)
    
    
    logger.info("********Appium Server Starting********")
    base.start_appium_server()
    
    
    android_driver=base.setUp()
    logger.info("********Android Driver created********")
    base.start_screen_record(android_driver,logger)
    
      
    logger.info("*********Mavid Device Setup beggining*********")
    android_driver.implicitly_wait(50)
    time.sleep(5)

    try:
        testCase.test_01_mavid_app_setup_positiveCase(android_driver,logger)
    except Exception:
        base.stop_screen_record(android_driver,logger)
        #Kill the Driver
        base.tearDown(android_driver)
        
        #stop the appium server programatically
        base.stop_appium_server()
        time.sleep(5)
        os.system("start /B start cmd.exe @cmd /k py  post_avs_fail.py")    
            
    
        
    try:
    
        logger.info("*********AVS Login Starts*********")
        avs_Login.avs_login(android_driver,logger)
        
    except Exception: 
    
        base.stop_screen_record(android_driver,logger)
        #Kill the Driver
        base.tearDown(android_driver)       
        #stop the appium server programatically
        base.stop_appium_server()
        time.sleep(5)
        
        os.system("start /B start cmd.exe @cmd /k py post_avs_fail.py")
        
        
    base.stop_screen_record(android_driver,logger)
    logger.info("*********Killing Android Driver*********")
    base.tearDown(android_driver)
    
    logger.info("*********Killing Appium Server*********")
    base.stop_appium_server()
    
    time.sleep(2)
    #os.system("start /B start cmd.exe @cmd /k py post_avs_fail.py")
      
        
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_LIBRE_MAVID_APP)
    unittest.TextTestRunner(verbosity=2).run(suite)