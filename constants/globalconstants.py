from selenium.webdriver.common.by import By

BASE_URL = "https://open.spotify.com/"
REGISTER_BUTON = (By.CLASS_NAME, "Button-sc-1dqy6lx-0.ljUEiq.sibxBMlr_oxWTfBrEz2G")
COOKIE_ACCEPT_LOCATE = (By.ID, "onetrust-accept-btn-handler")
REGISTER_MAIL_LOCATE = (By.ID, "username")
CONTINUE_BUTTON_LOCATE1 = (By.CLASS_NAME, "Button-sc-qlcn5g-0.cUOgcY")
REGISTER_PASSWORD_LOCATE = (By.ID, "new-password")
REGSITER_NAME_LOCATE = (By.ID, "displayName")
DATE_TIME_DAY_LOCATE = (By.ID, "day")
DATE_TIME_MONTH_LOCATE = (By.ID, "month")
DATE_TIME_YEAR_LOCATE = (By.ID, "year")
MALE_GENDER_LOCATE = (By.CLASS_NAME, "Indicator-sc-hjfusp-0.jeEHZA")
MARKETING_BOX_LOCATE = (By.CLASS_NAME, "Label-sc-cpoq-0.havZVP")
PRIVACY_BOX_LOCATE = (By.CSS_SELECTOR, "label[for='checkbox-privacy'].Label-sc-cpoq-0.havZVP")
PROFILE_PIC_LOCATE = (By.CLASS_NAME, "Button-sc-1dqy6lx-0.hpNmgY.encore-over-media-set.SFgYidQmrqrFEVh65Zrg")




##TEST DATA##

REGISTER_MAIL = ("coss2erep@smallmtn.lol")
PASSWORD = ("testdata123")
NAME = ("Mehmet")
DAY = ("28")
MONTH = "//*[@id='month']/option[13]"
YEAR = ("1994")