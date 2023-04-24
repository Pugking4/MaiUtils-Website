from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options


options = webdriver.ChromeOptions()
#options.add_argument("--headless")
options = Options()
# browser is Chromium instead of Chrome
options.BinaryLocation = "/usr/bin/chromium-browser"
# we use custom chromedriver for raspberry
driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(service=Service(driver_path))

driver.get('https://www.google.com')

print("bruh")

Service(driver_path).stop()
