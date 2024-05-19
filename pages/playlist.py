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