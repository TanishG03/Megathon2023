from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import time

driver = webdriver.Firefox()
driver.maximize_window()

url = "https://www.facebook.com/"
driver.get(url)

# Wait for the login form to be visible
wait = WebDriverWait(driver, 10)

login_form = wait.until(EC.presence_of_element_located((By.ID, "session_key")))

username = "aadityavardhan.avna@gmail.com"
password = "aaditya-123"

# Enter username and password
username_field = driver.find_element(By.ID, 'email')
username_field.send_keys(username)

password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)