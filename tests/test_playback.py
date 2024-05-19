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
class TestPlayback(softest.TestCase, unittest.TestCase):

    def test_play_a_song(self):
        playback = Playback(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        sleep(1)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        playback.click_search_button()
        playback.search_a_song()
        playback.click_song_img()
        self.soft_assert(self.assertEqual,playback.assert_paused_song(),PAUSED_ICON_TEXT, "The data is not matching")
        self.assert_all()
        sleep(3)

    def test_pause_a_song(self):
        playback = Playback(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        sleep(1)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        playback.click_search_button()
        playback.search_a_song()
        playback.click_song_img()
        playback.click_footer_play_button()
        self.soft_assert(self.assertEqual,playback.assert_continue_song(),PLAY_ICON_TEXT, "The data is not matching")
        self.assert_all()

    def test_skip_a_song(self):
        playback = Playback(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        sleep(1)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        playback.click_search_button()
        playback.search_a_song(),
        playback.click_song_img()
        playback.click_skip_song_button()
        self.soft_assert(self.assertNotEqual,playback.assert_song_name(),RAMMSTEIN_SONG_TEXT, "The data is matching.Song is not skipped")
        self.assert_all()
        