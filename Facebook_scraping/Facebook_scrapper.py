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

login_form = wait.until(EC.presence_of_element_located((By.ID, "email")))

username = "vishal.tanish50@gmail.com"
password = "TanishG2003"

# Enter username and password
username_field = driver.find_element(By.ID, 'email')
username_field.send_keys(username)

password_field = driver.find_element(By.ID, 'pass')
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

time.sleep(10)

profile_url = "https://www.facebook.com/markangelcomedy/"

driver.get(profile_url)

#to get the post data of the person
page_source = driver.page_source
soup = BS(page_source, features='html.parser')

driver.execute_script("window.scrollTo(0, 4000);")

time.sleep(2)
driver.execute_script("window.scrollTo(0, 4000);")

time.sleep(2)
driver.execute_script("window.scrollTo(0, 4000);")
time.sleep(2)


driver.execute_script("window.scrollTo(0, 4000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
time.sleep(2)
with open('post.html', 'w') as f:
    f.write(str(soup))

#to get the about of the data
driver.get(profile_url+"about")
driver.execute_script("window.scrollTo(0, 4000);")
time.sleep(2)
with open('about.html', 'w') as f:
    f.write(str(soup))


