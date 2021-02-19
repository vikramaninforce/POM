import pytest
from pages.loginpage import LoginPage
from selenium import webdriver


class Test_1_login:
    baseUR = "https://instacolrwebfedev.eu-de.mybluemix.net/"
    baseURL = "https://letskodeit.teachable.com/p/practice"
    username = "check"
    def test_login(self, setup):
        self.driver = webdriver.Chrome(executable_path="/dev/chromedriver")
        self.driver.get(self.baseUR)
        self.driver.implicitly_wait(30)
        # self.driver.get(self.baseURL)
        self.lp = LoginPage(self.driver)
        self.lp.setUserName(self.username)

# l=Test_1_login()
# l.test_login()