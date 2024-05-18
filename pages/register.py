import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from pages.PageBase import PageBase
from constants.globalconstants import *



@pytest.mark.usefixtures("setup")
class Register(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def accept_cookies(self):
        cookies = self.wait_element_visibility(COOKIE_ACCEPT_LOCATE)
        cookies.click()

    def click_register_button(self):
        register_buton = self.wait_element_visibility(REGISTER_BUTON)
        register_buton.click()

    def fill_mail_information(self):
        mail_location = self.wait_element_visibility(REGISTER_MAIL_LOCATE)
        mail_location.send_keys(REGISTER_MAIL)
        sleep(1)

    def click_continue_button1(self):
        continue_button = self.wait_element_visibility(CONTINUE_BUTTON_LOCATE1)
        continue_button.click()
    
    def fill_password_information(self):
        password_info = self.wait_element_visibility(REGISTER_PASSWORD_LOCATE)
        password_info.send_keys(PASSWORD)
        sleep(1)
    
    def click_continue_button_long_sleep(self):
        continue_button2 = self.wait_element_visibility(CONTINUE_BUTTON_LOCATE1)
        continue_button2.click()
        sleep(10)

    def fill_name_information(self):
        name_info = self.wait_element_visibility(REGSITER_NAME_LOCATE)
        name_info.send_keys(NAME)
    
    def fill_date_of_birth(self):
        birth_day_info = self.wait_element_visibility(DATE_TIME_DAY_LOCATE)
        birth_day_info.send_keys(DAY)
        birth_month_info = self.wait_element_visibility(DATE_TIME_MONTH_LOCATE)
        select_month = Select(birth_month_info)
        select_month.select_by_value("12")
        birth_year_info = self.wait_element_visibility(DATE_TIME_YEAR_LOCATE)
        birth_year_info.send_keys(YEAR)

    def select_gender(self):
        select_gender = self.wait_element_visibility(MALE_GENDER_LOCATE)
        select_gender.click()

    def accept_marketing(self):
        marketing_button = self.wait_element_visibility(MARKETING_BOX_LOCATE)
        marketing_button.click()
        sleep(1)
    
    def accept_privacy(self):
        privacy_button = self.wait_element_visibility(PRIVACY_BOX_LOCATE)
        privacy_button.click()
        sleep(2)

    def assert_spotify_profile(self):
        profile_button = self.wait_element_visibility(PROFILE_PIC_LOCATE)
        get_label = profile_button.get_attribute('aria-label')
        return get_label

    