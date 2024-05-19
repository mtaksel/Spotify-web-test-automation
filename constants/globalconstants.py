from selenium.webdriver.common.by import By


##REGISTER##

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

##LOGIN##

LOGIN_BUTTON_LOCATE = (By.XPATH, "//*[@id='main']/div/div[2]/div[3]/header/div[2]/div[3]/div[1]/button[2]")
LOGIN_MAIL_LOCATE = (By.ID, "login-username")
LOGIN_PASSWORD_LOCATE = (By.ID, "login-password")
SIGNIN_BUTTON_LOCATE = (By.CLASS_NAME, "ButtonInner-sc-14ud5tc-0.liTfRZ.encore-bright-accent-set")
ERROR_TEXT_LOCATE = (By.CLASS_NAME, "Message-sc-15vkh7g-0.dHbxKh")
INVALID_LOGIN_ERROR_TEXT = "Kullanıcı adı veya parola yanlış."
LOGOUT_BUTTON_LOCATE = (By.CLASS_NAME, "Type__TypeElement-sc-goli3j-0.dsbIME.ellipsis-one-line.htqz7Vb8mLJvGKTi1vrs")

##PLAYBACK##

SEARCH_BUTTON_LOCATE = (By.CLASS_NAME, "Svg-sc-ytk21e-0.bneLcE.search-icon.QbaKKdcHNA2x3_YJvpYu")
SEARCH_BOX_LOCATE = (By.CLASS_NAME, "encore-text.encore-text-body-small.NtkAQg9R1r5CjuP0XHwl")
IMG_PLAY_BUTTON = (By.CLASS_NAME, "Svg-sc-ytk21e-0.bneLcE.zOsKPnD_9x3KJqQCSmAq")
PAUSED_ICON_TEXT = ("Duraklat")
PLAY_ICON_TEXT = ("Çal")
PLAY_ICON_LOCATE = (By.CLASS_NAME, "vnCew8qzJq3cVGlYFXRI")
HOVER_BUTTON = (By.CLASS_NAME, "IjYxRc5luMiDPhKhZVUH.UpiE7J6vPrJIa59qxts4.ZgAJecvDDVREPXktThbA")
FOOTER_PLAY_BUTTON = (By.CLASS_NAME, "vnCew8qzJq3cVGlYFXRI")
SKIP_ICON_LOCATE = (By.CLASS_NAME, "mnipjT4SLDMgwiDCEnRC")
FOOTER_SONG_NAME_LOCATE = (By.CLASS_NAME, "deomraqfhIAoSB3SgXpu")
RAMMSTEIN_SONG_TEXT = ("Şu anda çalan: Rammstein tarafından Sonne")


##TEST DATA##

LOGIN_MAIL = ("coss2erep@smallmtn.lol")
REGISTER_MAIL = ("coss2erep@smallmtn.lol")
PASSWORD = ("testdata123")
NAME = ("Mehmet")
DAY = ("28")
MONTH = "//*[@id='month']/option[13]"
YEAR = ("1994")
TEST_SEARCH_SONG = ("rammstein")