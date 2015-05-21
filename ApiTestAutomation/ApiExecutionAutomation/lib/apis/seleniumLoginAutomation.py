from pyvirtualdisplay import Display
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re
#import ConfigFileProduction
#import ConfigFileStaging
#import ConfigFile
import variables
import sys

redirectURL = ""
authorization_url= ""
#user_email = "mchowla@rubiconproject.com"
#user_password = "Mike2015!"
#organization = "Mealtime media"

class SeleniumMasheryTest(unittest.TestCase):

    def setUp(self):
        #print "In setup"
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        #self.URL = urlData.URL
        #self.URL = "http://dspbuilder.rubiconproject.com/login?response_type=code&client_id=zfupgaj4k7ashk2wx635zptm&redirect_uri=http%3A%2F%2Frubiconproject.mashery.com%2Fio-docs%2Foauth2callback&state=icOrp52N44RdW4JAMhaKQFWQPaiGqB"
        #self.base_url = "http://dspbuilder.rubiconproject.com/"
        self.verificationErrors = []
        self.accept_next_alert = True



    def test_selenium_mashery(self):

        global redirectURL
        global authorization_url
        #print "In test_selenium_mashery"
        driver = self.driver
        driver.get(authorization_url)
        #driver.get(self.base_url + "/login?response_type=code&client_id=zfupgaj4k7ashk2wx635zptm&redirect_uri=http%3A%2F%2Frubiconproject.mashery.com%2Fio-docs%2Foauth2callback&state=icOrp52N44RdW4JAMhaKQFWQPaiGqB")
        driver.find_element_by_id("user_email").clear()
        #driver.find_element_by_id("user_email").send_keys("mchowla@rubiconproject.com")
        #print variables.ConfigFile.user_email, variables.ConfigFile.user_password, variables.ConfigFile.organization
	driver.find_element_by_id("user_email").send_keys(variables.ConfigFile.user_email)
	driver.find_element_by_id("user_password").clear()
        driver.find_element_by_id("user_password").send_keys(variables.ConfigFile.user_password)
        driver.find_element_by_name("commit").click()
        Select(driver.find_element_by_id("organization")).select_by_visible_text(variables.ConfigFile.organization)
        driver.find_element_by_name("commit").click()
        #driver.get(link)
        #print("Redirected url : " + driver.current_url)
        redirectURL = driver.current_url
        #print "Redirected url : " + redirectURL

    def is_element_present(self, how, what):
        #print "is_element_present"
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True

    def is_alert_present(self):
        #print "is_alert_present"
        try: self.driver.switch_to_alert()
        except NoAlertPresentException, e: return False
        return True

    def close_alert_and_get_its_text(self):
        #print "close_alert_and_get_its_text"
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
        #print "tearDown"
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)


def login_automation(auth_url):

    global redirectURL
    global authorization_url
    display = Display(visible=0, size=(1024, 768))
    display.start()
    authorization_url = auth_url

    #print "Accessing Authorization URL"

    suite = unittest.TestLoader().loadTestsFromTestCase(SeleniumMasheryTest)
    unittest.TextTestRunner().run(suite)

    display.stop()
    #print "redirectURL = " + redirectURL
    return redirectURL

#r = login_automation("http://dspbuilder.rubiconproject.com/login?response_type=code&client_id=zfupgaj4k7ashk2wx635zptm&redirect_uri=http%3A%2F%2Frubiconproject.mashery.com%2Fio-docs%2Foauth2callback&state=icOrp52N44RdW4JAMhaKQFWQPaiGqB")

#print "r = " + r

