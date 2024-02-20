from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import calc

url = 'http://suninjuly.github.io/explicit_wait2.html'

with webdriver.Chrome() as browser:
    browser.get(url)

    price = WebDriverWait(browser, 12).until(EC.text_to_be_present_in_element((By.ID, "price"), "$100"))
    print('Good price')
    browser.find_element(By.ID, 'book').click()

    calc.calc(browser)
    print('Done!')

    time.sleep(5)
