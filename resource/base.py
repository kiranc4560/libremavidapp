import os
import subprocess
from appium import webdriver
from selenium.webdriver.common.by import By
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base64
import time

def start_appium_server():
    os.system("start /B start cmd.exe @cmd /k appium --relaxed-security --log-timestamp --log appium.log  -a 127.0.0.1 -p 4723")
  
def working_dri():
    cwd=os.getcwd()
    return cwd
    
    
def android_info(command):
    #return os.system(command)
    device_info=subprocess.Popen(command, shell=False)
    return device_info.communicate()
    

def setUp():
    "Setup for the test"
    desired_caps = {}
    desired_caps['automationName'] = 'UiAutomator2'
    desired_caps['browserName '] = 'Chrome'
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] ='10.0.0'
    desired_caps['deviceName'] = '$'+ str(android_info('adb get-serialno')[0])
    # Since the app is already installed launching it using package and activity name
    desired_caps['appPackage'] = 'com.libre.irremote'
    desired_caps['appActivity'] = 'com.libre.irremote.SplashScreenActivity'
    # Adding appWait Activity since the activity name changes as the focus shifts to the ATP WTA app's first page
    #desired_caps['appWaitActivity'] ='com.hama_sirium.ActiveScenesListActivity' #'com.libre.irremote.irActivites.IRSignUpLoginWebViewActivity'
    desired_caps['noReset '] = 'true'
    #desired_caps['autoWebview '] = 'true'
    desired_caps['chromedriverExecutable'] = working_dri()+"\webdrivers\chromedriver.exe"
    #desired_caps['chromeOptions'] = {'androidUseRunningApp': True, 'w3c': False}
    desired_caps['setWebContentsDebuggingEnabled '] = 'true'
    desired_caps['autoGrantPermissions'] = 'true'
       
    return webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)


screenrecordings=working_dri()+"\screenrecordings" 

def start_screen_record(driver,logger):
    driver.start_recording_screen()
    logger.info("****Start Recording the App Screen****")

def stop_screen_record(driver, logger): 
    screen_record=driver.stop_recording_screen()
    video_Name=driver.current_activity+time.strftime("%Y_%m_%d_%H%M%S")
    fileName = os.path.join(screenrecordings,video_Name+".mp4")
    with open(fileName, 'wb') as vd:
        vd.write(base64.b64decode(screen_record))
    logger.info("****screen recording stored in the following path screenrecordings\\"+video_Name+".mp4"+"****")

def tearDown(driver):
    driver.quit()
        
def stop_appium_server():
    os.system("taskkill /F /IM node.exe")
    os.system("taskkill /F /IM cmd.exe")

def wait_for_element_to_be_clickable(driver, locator, elem, sleep=10):
    eleme = WebDriverWait(driver, sleep).until(EC.element_to_be_clickable((By.locator, elem)))
    return eleme
        
def wait_for_element_to_be_locate(driver, locator, elem, sleep=10):
    eleme = WebDriverWait(driver, sleep).until(EC.presence_of_element_located((By.locator, elem)))
    return eleme
        
    
def tap_on_element(driver, element, sleep=3):
    actions = TouchAction(driver)
    actions.tap(element)
    actions.perform()
    time.sleep(sleep)