from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
import variables
import sys

redirectURL = ""
authorization_url= ""

class SeleniumMasheryTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.verificationErrors = []
        self.accept_next_alert = True

    def test_selenium_mashery(self):

        global redirectURL
        global authorization_url
        driver = self.driver
        driver.get(authorization_url)
        driver.find_element_by_id("user_email").clear()
	driver.find_element_by_id("user_email").send_keys(variables.ConfigFile.user_email)
	driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys(variables.ConfigFile.user_password)
        driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("organization")).select_by_visible_text(variables.ConfigFile.organization)
        driver.find_element_by_name("commit").click()
        redirectURL = driver.current_url

    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def login_automation(auth_url):

    global redirectURL
    global authorization_url
    display = Display(visible=0, size=(1024, 768))
    display.start()
    authorization_url = auth_url

    suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumMasheryTest)
    unittest.TextTestRunner().run(suite)

    display.stop()
    return redirectURL

