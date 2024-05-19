import pytest
from time import sleep
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.action_chains import ActionChains
from pages.PageBase import PageBase
from constants.globalconstants import *

@pytest.mark.usefixtures("setup")
class Playlist(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver

    def click_cross_icon(self):
        cross_icon = self.wait_element_visibility(CROSS_ICON_LOCATE)
        cross_icon.click()

    def create_playlist_button(self):
        create_playlist = self.wait_element_visibility(CREATE_PLAYLIST_BUTTON)
        create_playlist.click()
    
    def close_pop_up(self):
        pop_up = self.wait_element_visibility(POP_UP_LOCATE)
        pop_up.click()

    def assert_playlist_text(self):
        playlist_test = self.wait_element_visibility(PLAYLIST_TEXT_LOCATE)
        return playlist_test.text
    
    def search_song(self):
        search_bar = self.wait_element_visibility(SEARCH_BAR_LOCATE)
        search_bar.send_keys(TEST_SEARCH_SONG)

    def add_song_to_playlist(self):
        track1 = self.wait_element_visibility(ADD_TEST_SONG1)
        track1.click()
        track2 = self.wait_element_visibility(ADD_TEST_SONG2)
        track2.click()