from selenium import webdriver
import os
import sys
import configparser
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
counter = 0
config = configparser.ConfigParser()
config.read("/root/reddit_comment_reader/configuration/config.ini")
dirpath=config["general"]["home_directory"]
def generate(url, div_id, prefix, folder):
    print(div_id)
    chrome_options = Options()
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument("--window-size=1920,1080")
    #chrome_options.add_argument("start-maximized");
    chrome_options.add_argument("disable-infobars")
    chrome_options.add_argument("--disable-extensions")
    driver = webdriver.Chrome("/usr/lib/chromium-browser/chromedriver",options=chrome_options)
    print(url)
    driver.get(url)
    try:
        cookies = driver.find_elements_by_tag_name("form")
        cookies[1].submit()
        if driver.find_element_by_css_selector("button._2JBsHFobuapzGwpHQjrDlD"):
            driver.find_element_by_css_selector("button._2JBsHFobuapzGwpHQjrDlD").click()
        image = WebDriverWait(driver,20).until(EC.presence_of_element_located((By.ID,div_id)))
        image.screenshot(dirpath + '/' + folder + '/' + prefix + '.png')
    finally:
        driver.quit()
