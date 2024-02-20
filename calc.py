def calc(browser):
    from selenium.webdriver.common.by import By
    from math import log, sin
    x = int(browser.find_element(By.ID, 'input_value').text)
    result = log(abs(12 * sin(x)))
    browser.find_element(By.ID, 'answer').send_keys(result)
    browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()
    alert = browser.switch_to.alert
    answer = alert.text.split()[-1]
    print(answer)
    alert.accept()
