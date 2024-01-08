import time
from selenium import webdriver
import requests
from selenium.common.exceptions import WebDriverException as WDE
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import random
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.edge.service import Service
import Helpers as Hp
#import HtmlTestRunner



# Unittest with Chrome and Edge, 3 tests for each Browser


class ChromeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.maximize_window()

     # Positive Test <Verify LogIn Form >
    def test_1Login(self):
        driver = self.driver

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

        # Delay all actions from 1 to 3 sec
        delay()


    # Positive Test <Choose Product and add to Card>
    def test_2shop(self):
        driver = self.driver

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


    # Negative Test <Choose product without Color_button>

    def test_3Nshop(self):
        driver = self.driver


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


    def tearDown(self):
        self.driver.quit()



class EdgeBrowser(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Edge(service=Service(EdgeChromiumDriverManager().install()))
        self.driver.maximize_window()

        # Positive Test <Verify LogIn Form >
    def test_1Login(self):
        driver = self.driver


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
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.hpage_label)))
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.but_login)))

        # find button "Log In"
        driver.find_element(By.XPATH, Hp.but_login).click()
        delay()
        wait.until(EC.visibility_of_element_located((By.XPATH, Hp.but_login)))
        delay()
        driver.find_element(By.XPATH, Hp.but2_login).click()

        driver.find_element(By.XPATH, Hp.but_logWithEmail).click()
        time.sleep(7)


        # Fill Sig In Form
        driver.find_element(By.XPATH, Hp.imp_email).clear()
        driver.find_element(By.XPATH, Hp.imp_email).click()
        driver.find_element(By.XPATH, Hp.imp_email).send_keys( Hp.temp_email)
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

        # Delay all actions from 1 to 3 sec
        delay()


    # Positive Test <Choose Product and add to Card>
    def test_2shop(self):
        driver = self.driver

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

        # find button "Shop"
        driver.find_element(By.XPATH, Hp.Lab_shop).click()
        delay()

        # Choose product1 and add it to Card
        driver.find_element(By.XPATH, Hp.product1).click()
        delay()
        driver.find_element(By.XPATH, Hp.prod1_info)
        delay()
        driver.find_element(By.XPATH, Hp.quanty)
        driver.find_element(By.XPATH, Hp.color_blc).click()
        driver.find_element(By.XPATH, Hp.add_card).click()
        delay()

        driver.back()

        # API testing from Selenium
        print("Webpage Url has", requests.get(Hp.scm_url).status_code,"as status Code")

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

        # Delay all actions from 1 to 3 sec
        delay()

        # Negative Test <Choose product without Color_button>

    def test_3shop(self):
        driver = self.driver

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

        # Choose product1 without color and add it to Card

        driver.find_element(By.XPATH, Hp.quanty)
        time.sleep(2)
        # driver.find_element(By.XPATH, "//span[contains(@data-hook,'number-input-spinner-up-arrow')]").click()
        driver.find_element(By.XPATH, Hp.add_card).click()
        delay()

        color_err = driver.find_element(By.XPATH, Hp.Color_Err)
        if color_err:
            print('Select Color')
        else:
            print('Error different')

        driver.back()

        # API testing from Selenium
        print("Webpage Url has", requests.get(Hp.scm_url).status_code,
              "as status Code")
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



    def tearDown(self):
        self.driver.quit()



if __name__ == '__main__':
    unittest.main()

    # unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='./HtmlReports'))




