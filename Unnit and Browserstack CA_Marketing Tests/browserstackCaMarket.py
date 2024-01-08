import requests
from dotenv import load_dotenv
import os
from selenium import webdriver
import random
import time
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.options import Options as EdgeOptions
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException
from threading import Thread
from selenium.common.exceptions import WebDriverException as WDE
from BrowserStack import my_key   # Use your Key
import Helpers as  Hp


# load_dotenv()
BROWSERSTACK_USERNAME = os.environ.get("BROWSERSTACK_USERNAME") or my_key.BROWSERSTACK_USERNAME
BROWSERSTACK_ACCESS_KEY = os.environ.get("BROWSERSTACK_ACCESS_KEY") or my_key.BROWSERSTACK_ACCESS_KEY
URL = os.environ.get("URL") or "https://hub.browserstack.com/wd/hub"
BUILD_NAME = "browserstack-build-1"
capabilities = [
    {
        "browserName": "Chrome",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python CaMarket",  # test name
        "buildName": "BSPy CaMarket",  # Your tests will be organized within this build
    },
    {
        "browserName": "Edge",
        "browserVersion": "latest",
        "os": "Windows",
        "osVersion": "11",
        "sessionName": "BStack Python CaMarket",  # test name
        "buildName": "BSPy CaMarket",  # Your tests will be organized within this build
    }]




def get_browser_option(browser):
    switcher = {
        "chrome": ChromeOptions(),
        #"firefox": FirefoxOptions(),
        "edge": EdgeOptions(),
        #"safari": SafariOptions(),
    }
    return switcher.get(browser, ChromeOptions())


def run_session(cap):
    bstack_options = {
        "osVersion": cap["osVersion"],
        "buildName": cap["buildName"],
        "sessionName": cap["sessionName"],
        "userName": BROWSERSTACK_USERNAME,
        "accessKey": BROWSERSTACK_ACCESS_KEY
    }
    if "os" in cap:
        bstack_options["os"] = cap["os"]
    options = get_browser_option(cap["browserName"].lower())
    if "browserVersion" in cap:
        options.browser_version = cap["browserVersion"]
    options.set_capability('bstack:options', bstack_options)
    driver = webdriver.Remote(
        command_executor=URL,
        options=options)


    # Test1 Log In
    try:
        url = Hp.hcm_url
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.hcm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        # Delay all actions from 1 to 3 sec
        delay()

        # Driver waits until certain text will be visible
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located( (By.XPATH, Hp.hpage_text)))

        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.hpage_label)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.but_login)))

        # find button "Log In"
        driver.find_element(By.XPATH, Hp.but_login).click()
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.but2_login)))
        delay()

        driver.find_element(By.XPATH, Hp.but2_login).click()

        driver.find_element(By.XPATH, Hp.but_logWithEmail).click()
        time.sleep(7)

        # Fill Sig In Form
        driver.find_element(By.XPATH, Hp.imp_email).clear()
        driver.find_element(By.XPATH, Hp.imp_email).click()
        driver.find_element(By.XPATH, Hp.imp_email).send_keys(Hp.temp_email)
        time.sleep(2)

        driver.find_element(By.XPATH, Hp.imp_passw).clear()
        driver.find_element(By.XPATH, Hp.imp_passw).click()
        driver.find_element(By.XPATH, Hp.imp_passw).send_keys(Hp.val_passw)
        time.sleep(2)
        driver.find_element(By.XPATH, Hp.captcha).click()
        driver.find_element(By.XPATH, Hp.sub_login).click()
        time.sleep(5)



        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.hcm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')

    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')



    # Test2 Shop (Positive)

    try:
        url = Hp.hcm_url
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.hcm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        # Delay all actions from 1 to 3 sec
        delay()

        # Driver waits until certain text will be visible

        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.hpage_text)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_home)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_blog)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_servis)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.Lab_shop)))
        delay()

        # find button "Shop"
        driver.find_element(By.XPATH, Hp.Lab_shop).click()
        delay()

        # Choose product1
        driver.find_element(By.XPATH, Hp.product1).click()
        delay()
        driver.find_element(By.XPATH, Hp.prod1_info)
        delay()

        # Choose product1 color and add it to Card

        driver.find_element(By.XPATH, Hp.quanty)
        driver.find_element(By.XPATH, Hp.color_blc).click()
        driver.find_element(By.XPATH, Hp.add_card).click()
        delay()

        driver.back()

        # API testing from Selenium
        print("Webpage Url has", requests.get(Hp.scm_url).status_code, "as status Code")
        code = requests.get(Hp.scm_url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.scm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')

    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')

    # Stop the driver
    #driver.quit()


    # Test3 Shop (Negative)

    try:
        url = Hp.hcm_url
        driver.get(url)
        driver.maximize_window()
        driver.minimize_window()
        driver.maximize_window()

        # driver sleep from 1 to 3 seconds
        def delay():
            time.sleep(random.randint(1, 3))

        # API testing from Selenium
        print("Webpage Url has", requests.get(url).status_code, "as status Code")
        code = requests.get(url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.hcm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

        # Delay all actions from 1 to 3 sec
        delay()


        # Driver waits until certain text will be visible
        wait = WebDriverWait(driver, 3)
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.hpage_text)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_home)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_blog)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.lab_servis)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.Lab_shop)))
        delay()

        # find button "Shop"
        driver.find_element(By.XPATH,Hp.Lab_shop).click()
        delay()

        # Choose product1
        driver.find_element(By.XPATH,Hp.product1).click()
        delay()


        # Choose product1 without color and add it to Card

        driver.find_element(By.XPATH, Hp.quanty)
        time.sleep(2)
        #driver.find_element(By.XPATH, "//span[contains(@data-hook,'number-input-spinner-up-arrow')]").click()
        driver.find_element(By.XPATH, Hp.add_card).click()
        delay()


        color_err = driver.find_element(By.XPATH, Hp.Color_Err)
        if color_err:
            print('Select Color')
        else:
            print('Error different')

        driver.back()

        # API testing from Selenium
        print("Webpage Url has", requests.get(Hp.scm_url).status_code, "as status Code")
        code = requests.get(Hp.scm_url).status_code
        if code == 200:
            print("API response code is OK")
        else:
            print("API response code is not 200", "Current code is:", code)

        # Check current webpage Title with Exception functionality
        try:
            assert Hp.scm_title in driver.title
            print(driver.title)
        except WDE:
            print("Webpage is different, current Title is: ", driver.title)

    # driver.quit()


    except WebDriverException:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'elements failed to load"}}')

    except Exception:
        driver.execute_script(
            'browserstack_executor: {"action": "setSessionStatus", "arguments": {"status":"failed", "reason": "Some '
            'exception occurred"}}')

    # Stop the driver
    driver.quit()

for cap in capabilities:
    Thread(target=run_session, args=(cap,)).start()