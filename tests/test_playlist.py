from time import sleep
from ddt import ddt, data, unpack
from selenium import webdriver
from pages.login import *
from pages.register import *
from pages.playlist import *
import allure
import softest
import unittest
import pytest

@pytest.mark.usefixtures("setup")
@ddt
class TestPlaylist(softest.TestCase, unittest.TestCase):

    def test_create_new_playlist(self):
        playlist = Playlist(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        playlist.click_cross_icon()
        playlist.create_playlist_button()
        playlist.close_pop_up()
        self.soft_assert(self.assertEqual,playlist.assert_playlist_text(), PLAYLIST_TEXT , "The data is not matching.")
        self.assert_all()
        sleep(5)
    
    def test_add_song_to_playlist(self):
        playlist = Playlist(self.driver)
        login = Login(self.driver)
        register = Register(self.driver)
        register.accept_cookies()
        login.click_login_button()
        login.fill_login_informations()
        login.click_signin_button()
        playlist.click_cross_icon()
        playlist.create_playlist_button()
        playlist.close_pop_up()
        playlist.search_song()
        playlist.add_song_to_playlist()
