from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option('detach', True)

driver = webdriver.Chrome(options=chrome_options)
driver.get('https://secure-retreat-92358.herokuapp.com/')

driver.maximize_window()

first_name_input = driver.find_element(By.NAME, value='fName')
last_name_input = driver.find_element(By.NAME, value='lName')
email_input = driver.find_element(By.NAME, value='email')

first_name_input.send_keys('Luis')
last_name_input.send_keys('Rodriguez')
email_input.send_keys('l.r.p.2991@gmail.com')
email_input.send_keys(Keys.ENTER)

driver.quit()