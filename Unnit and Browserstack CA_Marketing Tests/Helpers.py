import random
import time
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver.support.wait import WebDriverWait

# from UnitTest import Helpers as Hp


# driver sleep from 1 to 3 or 5 second
def delay1_5():
    time.sleep(random.randint( 1, 5))


def delay1_3():
    time.sleep(random.randint(1, 3))


# Url
g_url = "https://www.google.com"

hcm_url = "https://qasvus.wixsite.com/ca-marketing"
scm_url = "https://qasvus.wixsite.com/ca-marketing/shop"

# Title
hcm_title ="Home | California Marcketing"
scm_title ="Shop | California Marcketing"

# Email (temp) and Password
temp_email = "cobojoh462@watrf.com"
val_passw = "lena5577"


# Locators Log In
hpage_text = "//span[contains(text(),'LET CALIFORNIA MARKETING GROW YOUR BUSINECS')]"
hpage_label = "//img[@alt='iot_sq.png']"
but_login = "//span[contains(.,'Log In')]"
but2_login = "//button[contains(text(),'Log In')]"
but_logWithEmail = "//button[contains(.,'Log in with Email')]"
imp_email = "//input[@id='input_input_emailInput_SM_ROOT_COMP771']"
imp_passw = "//input[@id='input_input_passwordInput_SM_ROOT_COMP771']"
captcha = "//body/div[@id='SITE_CONTAINER']/div[@id='main_MF']/div[6]/div[2]"
sub_login = "(//button[contains(.,'Log In')])[2]"

# locators Shop
lab_home = "//p[@id='comp-ldaaacya0label']"
lab_blog = "//p[@id='comp-ldaaacya1label']"
lab_servis = "//p[@id='comp-ldaaacya3label']"
Lab_shop = "//p[@class='foFAdY'][contains(.,'Shop')]"
product1 = "(//img[@alt='Product 1'])[2]"
quanty = "//input[@type='number']"
color_blc = "//span[contains(@data-hook,'number-input-spinner-up-arrow')]"
add_card = "//span[contains(text(),'Add to Card')]"
prod1_info = "//h2[contains(text(),'PRODUCT INFO')]"

Color_Err = "//div[contains(text(),'Select Color')]"



# Check API response code
def check_API_code(driver):
    code = requests.get(hcm_url).status_code
    if code == 200:
        print("Url has ", requests.get(hcm_url).status_code, " as status Code")
    else:
        print("API response code is not 200")


    # Verify Pages Title
def assert_title(driver, title):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.title_is(title))
    assert title in driver.title
    print("Page has", driver.title + " as Page title")
    # Screenshot of the page
    driver.get_screenshot_as_file(f"Page {title}.png")
    if not title in driver.title:
        raise Exception(f"Page {title} has wrong Title!")
