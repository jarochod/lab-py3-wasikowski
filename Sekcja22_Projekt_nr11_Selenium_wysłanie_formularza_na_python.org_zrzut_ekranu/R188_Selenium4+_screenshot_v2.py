from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# ------------------------
# konfiguracja
# ------------------------
HEADLESS = False  # ustaw na False, żeby widzieć przeglądarkę

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

# wpisz "django"
searchInput = driver.find_element(By.XPATH, '//*[@id="id-search-field"]')
searchInput.send_keys("django")

# kliknij "Submit"
searchbutton = driver.find_element(By.ID, "submit")
searchbutton.click()

# ------------------------
# czekaj aż załadują się wyniki wyszukiwania (maks do 10 sek)
# np. pojawi się lista wyników (div z klasą "list-recent-events menu")
WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
)

# ------------------------
# screenshoty (dopiero po załadowaniu wyników)
driver.save_screenshot("python.org.1.png")
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.2.png")

# Zadziala poprawnie tylko gdy (HEADLESS=True)
func = lambda arg: driver.execute_script("return document.body.parentNode." + arg)
driver.set_window_size(func("scrollWidth"), func("scrollHeight"))
driver.find_element(By.TAG_NAME, "body").screenshot("python.org.3.png")

# tylko w trybie widocznym (HEADLESS=False) zatrzymaj na chwilę, żeby obserwować
if not HEADLESS:
    time.sleep(5)

driver.quit()
