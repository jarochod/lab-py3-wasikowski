from selenium import webdriver
from selenium.webdriver.common.by import By
import os
import time

# ------------------------
# konfiguracja
# ------------------------
HEADLESS = True  # ustaw na False, żeby widzieć przeglądarkę
# ustaw na Tre, żeby widzieć przeglądarkę

# katalog roboczy
scripDir = os.path.dirname(__file__)
os.chdir(scripDir)

# opcje Chrome
options = webdriver.ChromeOptions()
if HEADLESS:
    options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

# ------------------------
# akcje w przeglądarce
# ------------------------
driver.get("https://python.org")

searchInput = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
searchInput.send_keys("django")

searchbutton = driver.find_element(By.ID, "submit")
searchbutton.click()

# ------------------------
# screenshoty
driver.save_screenshot("python.org.1.png")
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.2.png")

# execute_script uruchamia kod JavaScript w przeglądarce: scrollWidth i scrollHeight – dają pełne wymiary strony.
func = lambda arg: driver.execute_script("return document.body.parentNode." + arg) 
driver.set_window_size(func("scrollWidth"), func("scrollHeight"))
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.3.png")

# Zadziala poprawnie tylko gdy (HEADLESS=True)
# execute_script uruchamia kod JavaScript w przeglądarce: scrollWidth i scrollHeight – dają pełne wymiary strony.
func = lambda arg: driver.execute_script("return document.body.parentNode." + arg)
driver.set_window_size(func("scrollWidth"), func("scrollHeight"))
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.3.png")

# tylko w trybie widocznym (HEADLESS=False) zatrzymaj na chwilę, żeby obserwować
if not HEADLESS:
    time.sleep(5)

driver.quit()
