from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_options import ChromeOptions
import time

chrome_options = ChromeOptions().get_options()

driver = webdriver.Chrome(options=chrome_options)
driver.get('http://orteil.dashnet.org/experiments/cookie/')
driver.maximize_window()

cookie = driver.find_element(By.XPATH, value='//*[@id="cookie"]')

end = time.time() + (60 * 2)

while time.time() < end:
    cookie.click()

# driver.quit()
