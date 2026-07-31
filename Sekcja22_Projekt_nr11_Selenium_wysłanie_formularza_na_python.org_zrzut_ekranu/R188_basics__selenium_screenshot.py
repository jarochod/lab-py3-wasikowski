#R188. Projekt nr 12: Selenium, wysłanie formularza na python.org, zrzut ekranu

from selenium import webdriver # pip install selenium

# pip install webdriver-manager
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

import time
import os

scriptDir = os.path.dirname(__file__)
os.chdir(scriptDir)

options = Options()
options.headless = True

driver = webdriver.Chrome( ChromeDriverManager().install(), options=options )
driver.get("https://python.org")

driver.maximize_window()

searchInput = driver.find_element_by_xpath('//*[@id="id-search-field"]')
searchInput.send_keys("django")

buttonSubmit = driver.find_element_by_id("submit")
buttonSubmit.click()

driver.save_screenshot("python.org.1.png")
driver.find_element_by_tag_name("body").screenshot("python.org.2.png")

func = lambda arg: driver.execute_script("return document.body.parentNode.scroll"+arg)

driver.set_window_size( func("Width"), func("Height") )
driver.find_element_by_tag_name("body").screenshot("python.org.3.png")

#time.sleep(5)
driver.quit()