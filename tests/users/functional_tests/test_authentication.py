from django.contrib.staticfiles.testing import StaticLiveServerTestCase

# from selenium import webdriver

from selenium.webdriver.chrome.webdriver import WebDriver

# from selenium.webdriver.chrome.options import Options
# import os


class TestAuthentication(StaticLiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.selenium = WebDriver()
        # chrome_options = Options()
        # chrome_options.add_argument("--headless")
        # cls.selenium = webdriver.Chrome(options=chrome_options)
        # chrome_driver = os.getcwd() + "/chromedriver.exe"
        # print("HELLO" + chrome_driver)
        # cls.driver = webdriver.Chrome(
        # chrome_options=chrome_options,
        # executable_path=chrome_driver,
        # )
        # cls.selenium = webdriver.Chrome()
        cls.selenium.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super().tearDownClass()

    def test_login(self):
        self.selenium.get("%s%s" % (self.live_server_url, "/login/"))
        username_input = self.selenium.find_element_by_name("username")
        username_input.send_keys("user1@gmail.com")
        password_input = self.selenium.find_element_by_name("password")
        password_input.send_keys("password1234")
        self.selenium.find_element_by_class_name("btn").click()

    """@classmethod
    def test_google(cls):
        cls.driver.get("https://www.google.com")
        lucky_button = cls.driver.find_element_by_css_selector("[name=btnI]")
        lucky_button.click()"""
