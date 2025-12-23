import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import getpass

# The course URL, which should redirect to the login page
COURSE_URL = "https://onlinecourses.nptel.ac.in/noc25_cs103/course"
CHROMEDRIVER_PATH = "/usr/bin/chromedriver"

# Get user credentials
username = input("Enter your email: ")
password = input("Enter your password: ")

# Set up Selenium
options = webdriver.ChromeOptions()
# Must not be headless for manual CAPTCHA solving
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--window-size=1200,800') # Adjusted window size

service = Service(executable_path=CHROMEDRIVER_PATH)
driver = webdriver.Chrome(service=service, options=options)

try:
    print("Navigating to the login page...")
    driver.get(COURSE_URL)

    print("Entering username and password...")
    # Find fields by their ID, which is more reliable
    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'Email'))
    )
    email_input.send_keys(username)

    # The password field is likely named 'Password'
    password_input = driver.find_element(By.ID, 'Password')
    password_input.send_keys(password)

    # Pause for manual CAPTCHA solving
    input("\n>>> Please solve the CAPTCHA in the browser window, then press Enter here to continue...")

    print("Clicking the 'Sign in' button...")
    # The button seems to be inside a form, let's find it by type and text
    signin_button = driver.find_element(By.XPATH, '//button[contains(text(), "Sign in")]')
    signin_button.click()

    # After login, we should be on the course page.
    # Wait for the assessment links to appear.
    print("Login submitted. Waiting for assessment links...")
    assessment_links_present = WebDriverWait(driver, 30).until(
        EC.presence_of_all_elements_located((By.XPATH, "//a[contains(@href, 'assessment=')]" ))
    )

    if assessment_links_present:
        print("\nFound assessment links:")
        links = [link.get_attribute('href') for link in assessment_links_present]
        for link in links:
            print(link)
    else:
        print("\nNo assessment links found after login.")

except TimeoutException as e:
    print(f"\nAn operation timed out.")
    print("This could be due to incorrect credentials or other issues after the login attempt.")
    print("Saving a screenshot to screenshot.png to help debug.")
    driver.save_screenshot('screenshot.png')

finally:
    print("\nClosing browser.")
    driver.quit()