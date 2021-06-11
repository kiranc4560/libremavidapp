from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resource.base import tap_on_element
from resource import avs_Login
from resource.data import data
from resource import base
import time
import os  

def speaker_setup(driver, logger):
    no_connect_to_other_network= driver.find_element_by_android_uiautomator('new UiSelector().text("No, connect to other network")')
    logger.info("****Click no_connect_to_other_network****")
    tap_on_element(driver, no_connect_to_other_network,5)
        
        
    REFRESH = WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="REFRESH"]')))
    #driver.find_element(By.XPATH,'//android.widget.TextView[@text="REFRESH"]')
    logger.info("****Click REFRESH****")
    tap_on_element(driver,REFRESH,5)
  
      
                
    ssid_down_arrow =WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'com.libre.irremote:id/iv_down_arrow')))
    #driver.find_element(By.ID,'com.libre.irremote:id/iv_down_arrow')
    logger.info("****Click on Drop down Arrow to list the SSID****")
    tap_on_element(driver, ssid_down_arrow,4)
    
     
    
    
    ssid_name = driver.find_element(By.XPATH,'//android.widget.TextView[@text="'+str(data["ssid_name"])+'"]')
    logger.info("****Slecting the SSID"+" "+data['ssid_name']+"****")
    tap_on_element(driver, ssid_name,5) 
        
        
        
    wifi_password= driver.find_element_by_android_uiautomator('new UiSelector().text("Wi-Fi Password")')
    logger.info("****Enetering the WIFI Passowrd"+" "+data['wifi_password']+"****")
    wifi_password.send_keys(str(data['wifi_password']))
        
        
    NEXT= driver.find_element_by_android_uiautomator('new UiSelector().text("NEXT")')
    logger.info("****Click on NEXT****")
    tap_on_element(driver, NEXT)
        
    try:    
        alert_obj = WebDriverWait(driver, 180).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Configuration Successful"]')))
        if alert_obj.text=='Configuration Successful':
            setup_ok= driver.find_element_by_android_uiautomator('new UiSelector().text("Ok")')
            logger.info("****Click on OK ro accept the Success Connection Alert****")
            tap_on_element(driver, setup_ok)
            avs_Login.avs_login(driver, logger)
    except Exception:
        base.stop_screen_record(android_driver,logger)
        #Kill the Driver
        base.tearDown(android_driver)
        
        #stop the appium server programatically
        base.stop_appium_server()
        time.sleep(5)
        os.system("start /B start cmd.exe @cmd /k py post_avs_fail.py")
        
              
        
def test_01_mavid_app_setup_positiveCase(driver,logger):
    
    logger.info("****Mavid App Successfuly launched****")
    
    try:
        Active_device =driver.find_element(By.XPATH, '//android.widget.LinearLayout/android.widget.TextView[@text="'+str(data["Active_ssid_name"])+'"]')#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.LinearLayout[@index="0"]/android.widget.TextView[@text="'+str(data["ble_ssid_name"])+'"]')))
        if Active_device.text== str(data["Active_ssid_name"]):
            logger.info("****Device "+str(data["Active_ssid_name"])+" Already connected to wifi do AVS Login****")
            Active_device_settings=driver.find_element(By.ID,'com.libre.irremote:id/advancedSettings')
            logger.info("****Select Active Scene of MACID "+" "+str(data["Active_ssid_name"])+"****")
            tap_on_element(driver, Active_device_settings,6)
    
        login=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.ID, 'com.libre.irremote:id/tv_amazon_login')))#'//android.widget.LinearLayout[@id="ll_alexa_settings"]/android.widget.TextView[@index="2"]')))
        if login.text=='Log-In':
            logger.info("****If Avs Login not Done Click on Log-IN to proceed with the avs login****")
            tap_on_element(driver, login)
            avs_Login.avs_login(driver, logger)
        else:
            print("AVS Login SuccessFull")
            logger.info("****AVS Login SuccessFull****")
       
    except:
        #Click on Add Button on the Discover Screen
        btn_add = driver.find_element(By.ID,'com.libre.irremote:id/action_add')
        logger.info("****Click on Add****")
        tap_on_element(driver, btn_add)       
        try: 
            #Selecting BLE Enabled Device
            BLE_SSID =driver.find_element(By.XPATH, '//android.widget.LinearLayout[@index="0"]/android.widget.TextView[@text="'+str(data["ble_ssid_name"])+'"]')#WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.LinearLayout[@index="0"]/android.widget.TextView[@text="'+str(data["ble_ssid_name"])+'"]')))
            logger.info("****Click on BLE ssid"+str(data["ble_ssid_name"])+"****")
            tap_on_element(driver, BLE_SSID)
            #Do Connect the device to WIFI
            speaker_setup(driver,logger)
        except:
            #Click On other Setup Option
            other_setup_option =WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="Other Setup Option"]')))
            logger.info("****Click on Other Setup Option****")
            tap_on_element(driver, other_setup_option)
            try:
                #Click On WIFI Setting Button
                wf_settings = driver.find_element_by_android_uiautomator('new UiSelector().text("WI-FI SETTINGS")')
                tap_on_element(driver, wf_settings)
            
                SmartIR_softAP = driver.find_element_by_android_uiautomator('new UiSelector().text("'+str(data["device_macid"])+'")')
                logger.info("****Choose the Device MAC ID-"+" "+data['device_macid']+"****")
                tap_on_element(driver, SmartIR_softAP,4)
                
                # It is an alert suggest user to keep the select MACID or else change to WIFI network
                Keep_alert = driver.find_elements_by_android_uiautomator('new UiSelector().text("Keep")')
                if len(Keep_alert)>0:
                    logger.info("****Accepted the Keep Alert(appear only Redmi phone)****")
                    tap_on_element(driver, Keep_alert[0])
                    time.sleep(2)
                    driver.back()
                    logger.info("****Return to app from Selecting the mac id"+" "+data["device_macid"]+"****")
                    logger.info("****redirecting to Speaker setup****")
                    speaker_setup(driver, logger)
                else:
                    driver.back()
                    logger.info("****Return to app from Selecting the mac id"+" "+data["device_macid"]+"****")
                    time.sleep(2)
                    logger.info("****redirecting to Speaker setup****")
                    speaker_setup(driver, logger)
            except:
                speaker_setup(driver, logger)