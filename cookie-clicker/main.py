from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_options import ChromeOptions
import time

chrome_options = ChromeOptions().get_options()

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
driver.maximize_window()

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')


secs = time.time() + 5
end = time.time() + (60 * 5)


while time.time() < end:
    cookie.click()
    if time.time() >= secs:
        items_to_purchase = driver.find_elements(By.CSS_SELECTOR, value='div#store div')
        for i in range(8):
            print(items_to_purchase[i].get_attribute('class'))
            if items_to_purchase[i].get_attribute('class') == 'grayed':
                items_to_purchase[i-1].click()
                break
        secs = time.time() + 5


# driver.quit()
