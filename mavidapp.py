import unittest
from selenium.webdriver.common.by import By
from resource.data import data
import testCasenew
from datetime import datetime
from resource import base
import logging
import time
import os


 
class Android_LIBRE_MAVID_APP(unittest.TestCase):
    "Class to run tests against the Mavid App "
    #Create and configure logger
    tm=datetime.now().strftime("%m-%d-%Y %H%M%S")
    logging.basicConfig(filename=base.create_file("logs" ,"mavidApp_Automation_logs"+tm+".log"),
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
    android_driver.implicitly_wait(10)
    time.sleep(5)

    try:
        testCasenew.test_01_mavid_app_setup_positiveCase(android_driver,logger)
    except Exception:
        print('ERROR IN YOUR TEST PLEASE VERIFY IT')
#---START OF SCRIPT
if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(Android_LIBRE_MAVID_APP)
    unittest.TextTestRunner(verbosity=2).run(suite)