from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.login import *
from pages.register import *
from pages.playback import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestPlaylist(softest.TestCase, unittest.TestCase):

    def create_new_playlist(self):
        playlist = Playback(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()