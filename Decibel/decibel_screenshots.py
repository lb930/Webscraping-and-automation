from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import ElementClickInterceptedException
import os
from log_util import logger

download_dir = r'C:\Users\me\Documents\Projects\Decibel Automation\05 Screenshots'
cr_extension_dir = r'C:\Users\me\Documents\Projects\Decibel Automation\03 Chrome Extension\3.4.20.6_0.crx'

def set_chrome_options():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    prefs = {'download.default_directory': download_dir}
    chrome_options.add_experimental_option('prefs', prefs)
    chrome_options.add_extension(cr_extension_dir)
    return chrome_options

def get_decibel_screenshots(chrome_options=set_chrome_options()):

    log = logger()

    try:
        driver = webdriver.Chrome(
            ChromeDriverManager().install(), chrome_options=chrome_options)
        driver.maximize_window()
        wait = WebDriverWait(driver, 30)

        email = os.environ['DECIBEL_USER']
        pw = os.environ['DECIBEL_PW']

        driver.get("https://portal.decibel.com/Login")

        # Login
        x = wait.until(EC.presence_of_element_located((By.XPATH, '//div//input[@placeholder="Email"]')))
        x.send_keys(email)
        driver.find_element_by_xpath('//div//input[@placeholder="Password"]').send_keys(pw)
        driver.find_element_by_xpath('//button[@type="submit"]').click()
        log.info('Logged in')

        # Go to Analyze -> Heatmaps
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="Text_root__2Tc8P HeaderBar_item-label__G-T32 mod-16 mod-semibold mod-sub"]')))
        driver.find_elements_by_xpath('//span[@class="Text_root__2Tc8P HeaderBar_item-label__G-T32 mod-16 mod-semibold mod-sub"]')[2].click()
        time.sleep(1)
        driver.find_element_by_xpath('//a[@href="/Heatmaps"]').click()

        # Select yesterday's date
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//span[@class="menu-item-inactive fill hidden"]')))
        driver.find_elements_by_xpath('//span[@class="menu-item-inactive fill hidden"]')[1].click()
        # Date range
        try:
            wait.until(EC.presence_of_all_elements_located(
                (By.XPATH, '//span[@class="select2-chosen"]')))
            driver.find_elements_by_xpath(
                '//span[@class="select2-chosen"]')[0].click()
        except ElementClickInterceptedException:
            time.sleep(1)
            driver.find_elements_by_xpath('//span[@class="select2-chosen"]')[0].click()
        # Yesterday
        wait.until(EC.presence_of_all_elements_located((By.XPATH, '//div[@class="select2-result-label"]')))
        driver.find_elements_by_xpath('//div[@class="select2-result-label"]')[2].click()
        # Submit button
        submit_button = wait.until(EC.presence_of_element_located((By.XPATH, '//span[@class="label"]')))
        submit_button.click()
        time.sleep(8)

        # Click on accept tracking
        driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
        tracking = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="gl-cta gl-cta--primary gl-cta--full-width"]')))
        tracking.click()
        time.sleep(1)
        driver.switch_to_default_content()

        # Export button
        driver.find_elements_by_xpath('//span[@class="menu-item-inactive fill hidden"]')[8].click()

        # Take screenshot
        take_screenshot = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="cyan takescreenshot"]//span[@class="label"]')))
        take_screenshot.click()
        # Create screenshot
        create_screenshot = wait.until(EC.presence_of_element_located((By.XPATH, '//button[@class="button cyan success"]')))
        create_screenshot.click()
        log.info('Generating screenshot')
        time.sleep(50)  # generating the screenshot takes a while
        # Download screenshot and wait until download has been completed
        driver.find_elements_by_xpath('//i[@class="icon-download"]')[0].click()
        time.sleep(7)

        driver.close()
        log.info('Screenshot downloaded succesfully')
        log.info('\n')

    except Exception as err:
        log.exception(err)
        log.info('\n')
        raise

if __name__ == '__main__':
    get_decibel_screenshots()
