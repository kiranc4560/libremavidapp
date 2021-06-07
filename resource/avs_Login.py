from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from resource.base import tap_on_element
from resource.data import data
import time

##########################################################################################
def do_avs_login_return_to_home(driver, logger):
    #### this mathod is used to enter the avs credentials and retur to app active scene####
    
    #Clearing the Email textbox and enter the email#
    em=driver.find_element(By.XPATH, '//input[@name="email"]')
    em.send_keys(Keys.CONTROL + "a");
    em.send_keys(Keys.DELETE);
    time.sleep(1)
    em.send_keys(str(data['avs_email']))
    logger.info("****Cleared the Emain text and Entering the email"+data['avs_email']+"****")
    time.sleep(1)
    ###############################

    
    #Clearing the Password field and enter the password#
    pwd=driver.find_element(By.XPATH, '//input[@type="password"]')
    pwd.clear()
    time.sleep(1)
    pwd.send_keys(str(data['avs_password']))
    logger.info("****Cleared the Password text and Entering the Password"+data['avs_password']+"****")
    time.sleep(1)
    driver.hide_keyboard()
    logger.info("****Hide Keyboard****")
    time.sleep(1)  
    ################################
    
    
    # CLick on submit to return to app#
    driver.find_element(By.XPATH, '//input[@type="submit"]').click()
    logger.info("****Click on submit****")
    time.sleep(10)
    ###################################
    
    #Finding the allow button
    allow =driver.find_elements_by_xpath("//input[@name='acknowledgementApproved']")
    

    #When Avs was already logged in, as we return from submitting the avs credentials, 
    #we will return directly to app, we checking here Allow button visible or not.     
    if len(allow)==0:
        time.sleep(10)
        #Returning to App Native view.
        driver.switch_to.context('NATIVE_APP')
        logger.info("****Return to Native view from Web view successfully****")
        things_to_try=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Things to try"]')))
        if 'Things to try' == things_to_try.text:
            print("AVS Login Successfully done")
            logger.info("****AVS login done Successfully****")
        else:
            print('AVS Login Failed')
            logger.info("****AVS login Failed****")
         
        #If allow button visible click on to return to app native view
    else:
        allow[0].click()
        time.sleep(10)
        #Returning to App Native view.
        # switch back to native view
        driver.switch_to.context('NATIVE_APP')
        logger.info("****Return to Native view from Web view successfully****")
        
        things_to_try=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Things to try"]')))
       
        if 'Things to try' == things_to_try.text:
            print("AVS Login Successfully done")
            logger.info("****AVS login done Successfully****")
            time.sleep(30)
        else:
            print('AVS Login Failed')
            logger.info("****AVS login Failed****")
            time.sleep(30)
        
       
       
#################################################################################################3        
        
def check_for_avs_login_if_not_do_login(driver, logger):
    #click on Sign in wiht amazon 
    signin_with_amazon = WebDriverWait(driver, 60).until(EC.element_to_be_clickable((By.XPATH, '//android.widget.Button[@text="LOGIN WITH AMAZON"]')))
    logger.info("****Click on LOGIN WITH AMAZON****")
    tap_on_element(driver, signin_with_amazon,20)
     
    #Swithing to Web view for avs login 
    webview = driver.contexts[1]
    print(webview)
    driver.switch_to.context(webview)
    logger.info("****Successfully switched from Native mobile view to webview****")
    
    
    #Do logout if already AVS is logged in and re-login again
    time.sleep(2)
    allow =driver.find_elements_by_xpath("//input[@name='acknowledgementApproved']")
            
    if len(allow)==0:
        do_avs_login_return_to_home(driver, logger)
        
    else:
        print(allow[0].text)
        signOutBtn =driver.find_element_by_xpath("//a[@class='a-link-normal lwa-aui-navbar-no-underline']")
        signOutBtn.click()
        time.sleep(3)
        sign_out =driver.find_element_by_xpath("//a[@title='Sign Out']")
        logger.info("****Singing out from AVS login****")
        sign_out.click()
        time.sleep(3)
        do_avs_login_return_to_home(driver, logger)
     
        
        
     #AVS login Method
#####################################AVS Login starts from here############################################################################     
def avs_login(driver, logger):
    LOGIN_WITH_AMAZON = driver.find_elements_by_xpath('//android.widget.Button[@text="LOGIN WITH AMAZON"]')
    logger.info("****Device Setup Successfull and connected to"+str(data["ssid_name"])+" ****")
    if(driver.is_app_installed('in.amazon.mShop.android.shopping')):
        print('Yes, Amazon Shopping App installed in the client machine')
        logger.info("****Yes, Amazon Shopping App installed in the client machine, Avs credetials are being taked from the Amazon App ****")
        tap_on_element(driver, LOGIN_WITH_AMAZON[0],5)
        """time.sleep(40)
        webview = driver.contexts[1]    
        if webview=='WEBVIEW_chrome':
            print(webview)
            driver.switch_to.context(webview)
            logger.info("****Successfully switched from Native mobile view to webview****")
            time.sleep(2)
            logger.info("****Click Allow to enable the Accept the terms and regulations ****")
            allow =driver.find_element_by_xpath("//input[@name='acknowledgementApproved']")
            allow.click()
            things_to_try=WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Things to try"]')))
       
            if 'Things to try' == things_to_try.text:
                print("AVS Login Successfully done")
                logger.info("****AVS login done Successfully****")
                time.sleep(30)
            else:
                print('AVS Login Failed')
                logger.info("****AVS login Failed****")
                time.sleep(30)
        """
        things_to_try=WebDriverWait(driver, 60).until(EC.presence_of_element_located((By.XPATH, '//android.widget.TextView[@text="Things to try"]')))
       
        if 'Things to try' == things_to_try.text:
            print("AVS Login Successfully done")
            logger.info("****AVS login done Successfully****")
            time.sleep(30)
        else:
            print('AVS Login Failed')
            logger.info("****AVS login Failed****")
            time.sleep(30)
        
    else:
        print("No, Amamzon Shopping app is not installed on client machine")
        logger.info("****No, Amamzon Shopping app is not installed on client machine****")
        if len(LOGIN_WITH_AMAZON)>0:
            check_for_avs_login_if_not_do_login(driver, logger)
        else:
            sign_out = driver.find_element_by_id('com.libre.irremote:id/text_sign_out') 
            logger.info("****Click Sign out If AVS Login already done!!, Signing out and re-login****")
            tap_on_element(driver, sign_out)
            check_for_avs_login_if_not_do_login(driver, logger)
 
        