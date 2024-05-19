from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.login import *
from pages.register import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestLogin(softest.TestCase, unittest.TestCase):

    def test_valid_login(self):
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        self.soft_assert(self.assertEqual,register.assert_spotify_profile(),NAME, "The data is not matching")
        self.assert_all()
    
    def test_invalid_login(self):
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.click_signin_button()
        self.soft_assert(self.assertEqual,login.assert_error_text(),INVALID_LOGIN_ERROR_TEXT, "Error msg is not matching")
        self.assert_all()

    def test_logout(self):
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        register.click_spotify_profile()
        login.click_logout_button()
