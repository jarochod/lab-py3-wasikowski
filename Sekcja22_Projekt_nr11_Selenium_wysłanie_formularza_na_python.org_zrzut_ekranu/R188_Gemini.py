from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import time

# ------------------------
# konfiguracja
# ------------------------
HEADLESS = True  # ustaw na False, żeby widzieć przeglądarkę

# katalog roboczy - lepszy sposób na ścieżki
script_dir = os.path.dirname(os.path.abspath(__file__))

# opcje Chrome
options = webdriver.ChromeOptions()
if HEADLESS:
    options.add_argument("--headless=new")

driver = webdriver.Chrome(options=options)

try:
    # ------------------------
    # akcje w przeglądarce
    # ------------------------
    driver.get("https://python.org")

    wait = WebDriverWait(driver, 10)
    searchInput = wait.until(EC.presence_of_element_located((By.XPATH, '//*[@id="id-search-field"]')))
    searchInput.send_keys("django")

    searchButton = driver.find_element(By.ID, "submit")
    searchButton.click()

    # ------------------------
    # czekaj aż załadują się wyniki wyszukiwania (maks do 10 sek)
    # np. pojawi się lista wyników (div z klasą "list-recent-events menu")
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, "list-recent-events"))
    )


    # ------------------------
    # screenshoty
    # Zdjecie zrzutu WIDOCZNEGO obszaru, przed powiększeniem okna
    visible_screenshot_path = os.path.join(script_dir, "python.org.visible.png")
    driver.save_screenshot(visible_screenshot_path)
    print(f"Zapisano zrzut WIDOCZNEGO obszaru: {visible_screenshot_path}")

    # Powiększ okno, aby zrobić zrzut pełnej strony
    func = lambda arg: driver.execute_script("return document.body.parentNode." + arg)
    driver.set_window_size(func("scrollWidth"), func("scrollHeight"))

    # Zapis zrzutu PEŁNEJ strony, po powiększeniu okna
    full_page_screenshot_path = os.path.join(script_dir, "python.org.full.png")
    driver.save_screenshot(full_page_screenshot_path)
    print(f"Zapisano zrzut PEŁNEJ strony: {full_page_screenshot_path}")

finally:
    driver.quit()