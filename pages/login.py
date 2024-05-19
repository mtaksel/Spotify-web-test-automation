import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.globalconstants import *


@pytest.mark.usefixtures("setup")
class Login(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_login_button(self):
        click_button = self.wait_element_visibility(LOGIN_BUTTON_LOCATE)
        click_button.click()
        sleep(1)
    
    def fill_login_informations(self):
        fill_mail = self.wait_element_visibility(LOGIN_MAIL_LOCATE)
        fill_mail.send_keys(LOGIN_MAIL)
        fill_password = self.wait_element_visibility(LOGIN_PASSWORD_LOCATE)
        fill_password.send_keys(PASSWORD)
    
    def click_signin_button(self):
        signup_button = self.wait_element_visibility(SIGNIN_BUTTON_LOCATE)
        signup_button.click()
    
    def assert_error_text(self):
        msg_box = self.wait_element_visibility(ERROR_TEXT_LOCATE)
        return msg_box.text
    
    def click_logout_button(self):
        logout_button = self.wait_element_visibility(LOGOUT_BUTTON_LOCATE)
        logout_button.click()