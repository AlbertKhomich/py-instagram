from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import instabot

SIMILAR_ACCOUNT = '777777777'
LOGIN = "+7777777777"
PASSWORD = os.environ['password']

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

bot = instabot.InstaBot(driver, LOGIN, PASSWORD, SIMILAR_ACCOUNT)

bot.login()
bot.find_followers()
bot.follow()
