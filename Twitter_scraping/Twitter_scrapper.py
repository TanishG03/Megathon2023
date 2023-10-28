from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import time

driver = webdriver.Firefox()
driver.maximize_window()

print("Enter the URL:")
url = input()
driver.get(url)

time.sleep(2)
driver.execute_script("window.scrollTo(0, 2000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
with open('text.html', 'w') as f:
    f.write(str(soup))
    driver.execute_script("window.scrollTo(0, 2000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
with open('text.html', 'a') as f:
    f.write(str(soup))
    driver.execute_script("window.scrollTo(0, 2000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
with open('text.html', 'a') as f:
    f.write(str(soup))
    driver.execute_script("window.scrollTo(0, 2000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
with open('text.html', 'a') as f:
    f.write(str(soup))
    driver.execute_script("window.scrollTo(0, 2000);")
page_source = driver.page_source
soup = BS(page_source, features='html.parser')
with open('text.html', 'a') as f:
    f.write(str(soup))
