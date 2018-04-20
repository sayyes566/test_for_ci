from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

chrome = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.CHROME)
firefox = webdriver.Remote(
          command_executor='http://localhost:4444/wd/hub',
          desired_capabilities=DesiredCapabilities.FIREFOX) 
test_ip = sys.argv[1]
chrome.get('http://' + test_ip)
print(chrome.title)

firefox.get('http://' + test_ip)
print(firefox.title)

chrome.quit()
firefox.quit()
