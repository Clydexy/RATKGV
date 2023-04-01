from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import chromedriver_autoinstaller
import sys
import time

for i in sys.argv:
    if i == "?" or i == "-H":
        # Help
        print("==== Help ====")
        print("-C: Click on the checkbox")
        print("-I: Return the status of the checkbox")
        print("-H: Help")
        exit()

chrome_options = Options()
chrome_options.add_argument("--headless")

chromedriver_autoinstaller.install()

# Initiate the browsercorn hub
browser = webdriver.Chrome(options=chrome_options)
browser.get('https://lionel2.kgv.edu.hk/login/index.php')

# Authentication Keys
username = "PARENT USERNAME"
password = "PARENT PASSWORD"

# Console Log
print("==== Console Log ====")

# Send Authentication Details

browser.find_element(By.NAME, "username").send_keys(username)
browser.find_element(By.NAME, "password").send_keys(password)
print("Authentication Keys Sent")

# Sign In
browser.find_element(By.ID, "loginbtn").click()
print("Login Successful")
checkbox = browser.find_element(By.ID, "chk18913733")
for i in sys.argv:
    
    if i == "-C":
        # Click on Button
        if not checkbox.get_attribute(name="checked"):
            checkbox.click()
        time.sleep(1)
        print("Click Verifying ...")
        time.sleep(2)
        print("Click Vefified, Program Success" if checkbox.get_attribute(name="checked") else "Verification Failure. Attempt -I for verification")
    elif i == "-I":
        # Return status
        print("Clicked Already" if checkbox.get_attribute(
            name="checked") else "Not Clicked Yet")
if len(sys.argv) == 1:
    checkbox.click()
time.sleep(2)
print("Terminating Program...")
time.sleep(1)
print("""
Terminated
====================
""")
