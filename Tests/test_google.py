from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time


options = Options()
options.add_argument("--headless")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")


driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)

try:
    driver.get("https://www.google.com")
    time.sleep(1)

    search_box = driver.find_element(By.NAME, "q")
    search_box.send_keys("DevOps is awesome")
    search_box.submit()

    time.sleep(2)

    assert "DevOps" in driver.title
    print("Test passed")

except Exception as e:
    print("Test failed", e)


finally:
    driver.quit()