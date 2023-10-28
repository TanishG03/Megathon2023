from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from bs4 import BeautifulSoup as BS
import time

driver = webdriver.Firefox()
driver.maximize_window()

url = "https://www.linkedin.com/"
driver.get(url)

# Wait for the login form to be visible
wait = WebDriverWait(driver, 10)

login_form = wait.until(EC.presence_of_element_located((By.ID, "session_key")))

username = "aadityavardhan.avna@gmail.com"
password = "aaditya-123"

# Enter username and password
username_field = driver.find_element(By.ID, 'session_key')
username_field.send_keys(username)

password_field = driver.find_element(By.ID, 'session_password')
password_field.send_keys(password)

# Submit the login form
password_field.send_keys(Keys.RETURN)

# Wait for the login process to complete
# wait.until(EC.title_contains("LinkedIn"))
time.sleep(4)


# Now you can navigate to the profile URL and scrape the data
while (True):
    print("Enter the URL:")
    profile_url = input()
    
    driver.get(profile_url)

    time.sleep(5)
    # Extract the page source or perform scraping as needed
    # before everything we extract the basic page
    print("getting the page...")
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('basic.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting activities...")
    # eight we scrape the activities of this person
    driver.get(profile_url+'recent-activity/all/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('activities.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting experinces...")
    # first lets scrape the experince of the person
    driver.get(profile_url+'details/experience/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('experince.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting education...")
    # second lets scrape the education of the person
    driver.get(profile_url+'details/education/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('education.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting projects...")
    # third lets scrape the projects of the person
    driver.get(profile_url+'details/projects/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('projects.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting skills...")
    # fourth lets scrape the skills of the person
    driver.get(profile_url+'details/skills/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('skills.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting course taken...")
    # fifth we scrape the courses taken by this person
    driver.get(profile_url+'details/courses/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('courses.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting honors...")
    # sixth we scrape the honors of the person
    driver.get(profile_url+'details/honors/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('honors.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("getting test scores...")
    # seventh we scrape the test scores of the person
    driver.get(profile_url+'details/testscores/')
    time.sleep(5)
    page_source = driver.page_source
    soup = BS(page_source, features='html.parser')
    with open('testscores.html', 'w') as f:
        f.write(str(soup))

    time.sleep(2)
    print("YAY!!!")

# Perform scraping operations with BeautifulSoup here

# Don't forget to close the browser when you're done
driver.quit()
