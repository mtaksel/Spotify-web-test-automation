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
class Playback(PageBase):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
    
    def click_search_button(self):
        search_button = self.wait_element_visibility(SEARCH_BUTTON_LOCATE)
        search_button.click()

    def search_a_song(self):
        search_box = self.wait_element_visibility(SEARCH_BOX_LOCATE)
        search_box.send_keys(TEST_SEARCH_SONG)

    def click_song_img(self):
        hover_img = self.hover(HOVER_BUTTON)
        song_img = self.wait_element_visibility(IMG_PLAY_BUTTON)
        song_img.click()
        sleep(2)
        
    def assert_paused_song(self):
        paused_icon = self.wait_element_visibility(PLAY_ICON_LOCATE)
        get_label = paused_icon.get_attribute('aria-label')
        return get_label
    
    def assert_continue_song(self):
        continue_icon = self.wait_element_visibility(PLAY_ICON_LOCATE)
        get_label = continue_icon.get_attribute('aria-label')
        return get_label
    
    def click_footer_play_button(self):
        footer_pbutton = self.wait_element_visibility(FOOTER_PLAY_BUTTON)
        footer_pbutton.click()
        sleep(2)

    def click_skip_song_button(self):
        skip_button = self.wait_element_visibility(SKIP_ICON_LOCATE)
        skip_button.click()
        sleep(6)
    
    def assert_song_name(self):
        song_name = self.wait_element_visibility(FOOTER_SONG_NAME_LOCATE)
        get_label = song_name.get_attribute('aria-label')
        return get_label
    
    