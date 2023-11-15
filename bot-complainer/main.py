from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from chrome_options import ChromeOptions
import time

USERNAME = 'podestal2991'
PASSWORD = '13angulo'

chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())
driver.get('https://twitter.com/i/flow/signup')
driver.maximize_window()

time.sleep(5)
login_tag = driver.find_element(By.XPATH, value='//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[7]/span[2]/span/span')
login_tag.click()
# username_input = driver.find_element(By.XPATH, value='/html/body/div/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
# time.sleep(5)
# username_input.send_keys(USERNAME)
# username_input.send_keys(Keys.ENTER)

time.sleep(5)
username_input = driver.find_element(By.XPATH, value='//*[@id="react-root"]/div/div/div/main/div/div/div/div[2]/div[2]/div/div[5]/label/div/div[2]/div/input')
username_input.send_keys(USERNAME)