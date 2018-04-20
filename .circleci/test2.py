from selenium import webdriver
import unittest
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import sys

class SearchText(unittest.TestCase):
   def setUp(self):
        # create a new session
        self.chrome = webdriver.Remote(
            command_executor='http://localhost:4444/wd/hub',
            desired_capabilities=DesiredCapabilities.CHROME)
        test_ip = sys.argv[1]
        self.chrome.get('http://' + test_ip)
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
        # navigate to the application home page
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self):
        lists = self.driver.find_elements_by_class_name("w10")
        no=len(lists)
        self.assertEqual(10, len(lists))
        
   def tearDown(self):
        # close the browser window
        self.chrome.quit()
        
 if __name__ == '__main__':
    test_ip = sys.argv[1]
    unittest.main()
