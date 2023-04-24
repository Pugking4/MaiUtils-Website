from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

options = Options()
# browser is Chromium instead of Chrome
options.BinaryLocation = "/usr/bin/chromium-browser"
# we use custom chromedriver for raspberry
driver_path = "/usr/bin/chromedriver"
driver = webdriver.Chrome(options=options, service=Service(driver_path))

driver.get("https://stackoverflow.com/")

print("bruh")