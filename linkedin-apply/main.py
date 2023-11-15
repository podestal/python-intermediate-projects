from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chrome_options import ChromeOptions
import time

chrome_options = ChromeOptions()
driver = webdriver.Chrome(options=chrome_options.get_options())
driver.maximize_window()

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
driver.get('https://www.linkedin.com/jobs/search/?currentJobId=3740965769&f_AL=true&keywords=Data%20entry%20remote&origin=JOB_SEARCH_PAGE_JOB_FILTER')
time.sleep(5)
apply_button = driver.find_element(By.CSS_SELECTOR, value='div.jobs-apply-button--top-card button')
print(apply_button.text)
apply_button.click()

time.sleep(5)
send = driver.find_element(By.CSS_SELECTOR, value='div button.artdeco-button')
send.click()

driver.quit()