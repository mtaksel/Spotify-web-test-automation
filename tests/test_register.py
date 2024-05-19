from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.register import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestRegister(softest.TestCase, unittest.TestCase):
    
    # Test Steps:
    # Accept cookies.
    # Click Register button.
    # Enter a valid email address.
    # Enter a valid password.
    # Enter a profile name.
    # Select a date of birth.
    # Select a gender.
    # Accept Marketing box
    # Accept Privacy box
    # Click on the "Sign Up" button.
    # Verify register name from profile

    def test_valid_register(self):
        register = Register(self.driver)
        register.accept_cookies()
        register.click_register_button()
        register.fill_mail_information()
        register.click_continue_button1()
        register.fill_password_information()
        register.click_continue_button1()
        register.fill_name_information()
        register.fill_date_of_birth()
        register.select_gender()
        register.click_continue_button1()
        register.accept_marketing()
        register.accept_privacy()
        register.click_continue_button1()
        register.assert_spotify_profile()
        self.soft_assert(self.assertEqual,register.assert_spotify_profile(),NAME, "The data is not matching")
        self.assert_all()
        