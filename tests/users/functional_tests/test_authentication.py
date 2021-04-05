from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

# from selenium.webdriver.firefox.webdriver import WebDriver

# from selenium.webdriver.firefox.options import Options
import os


class SeleniumRegisterTest(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        
        #firefox_options = Options()
        #firefox_options.add_argument("--headless")
        geckodriver = os.getcwd() + "/geckodriver"
        #cls.selenium = webdriver.Firefox(executable_path=geckodriver, options=firefox_options)
        cls.selenium = webdriver.Firefox(executable_path=geckodriver)
        cls.selenium.implicitly_wait(10)

        # FONCTIONNE
        #geckodriver = os.getcwd() + "/geckodriver"
        #driver = webdriver.Firefox(executable_path=geckodriver)
        #print("Firefox Browser Invoked")
        #driver.get('http://google.com/')
        #driver.quit()
        # FIN DE FONCTIONNE


    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()
    
    def test_register(self):
        # Access register page and fill fields
        self.selenium.get("%s%s" % (self.live_server_url, "/register/"))
        email_input = self.selenium.find_element_by_name("email")
        email_input.send_keys("usertest1@email.com")
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("usertest1")
        password_input = self.selenium.find_element_by_name("password1")
        password_input.send_keys("Password+1234")
        confirm_password_input = self.selenium.find_element_by_name("password2")
        confirm_password_input.send_keys("Password+1234")
        # Click on button which registers + login automatically
        self.selenium.find_element_by_class_name("btn").click()
        # Checks if icon "mon_compte" in DOM, means logged in
        self.selenium.find_element_by_id("mon_compte")

    """def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("user1@gmail.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password1234")
        self.selenium.find_element_by_class_name("btn").click()"""
