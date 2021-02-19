class Login:
    # Login Page
    # textbox_username_id = "Email"
    # textbox_password_id = "Password"
    # button_login_xpath = "//input[@value='Log in']"
    # link_logout_linktext = "Logout"

    def __init__(self,driver):
        self.driver=driver

    def userName(self):
        # return self.driver.find_element_by_id("name")
        return self.driver.find_element_by_name("email")

    # def password(self):
    #     self.driver.find_element_by_id(self.textbox_password_id)
    #
    # def clickLogin(self):
    #     self.driver.find_element_by_xpath(self.button_login_xpath).click()
    #
    # def clickLogout(self):
    #     self.driver.find_element_by_link_text(self.link_logout_linktext).click()