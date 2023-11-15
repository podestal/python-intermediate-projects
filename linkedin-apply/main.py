from selenium import webdriver
from selenium.webdriver.common.by import By
from chrome_options import ChromeOptions
import time

chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())

# Login Automatically
driver.get('https://www.linkedin.com')
email = driver.find_element(By.XPATH, value='//*[@id="session_key"]')
email.send_keys('l.r.p.2991@gmail.com')

password = driver.find_element(By.XPATH, value='//*[@id="session_password"]')
password.send_keys('13anguloX!')

time.sleep(3)
signin_button = driver.find_element(By.XPATH, value='//*[@id="main-content"]/section[1]/div/div/form/div[2]/button')
signin_button.click()

# Apply for a Job
# Apply for all the jobs

# driver.quit()