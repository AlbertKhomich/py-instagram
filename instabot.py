from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains


class InstaBot:
    def __init__(self, driver: webdriver.Chrome, login, password, similar):
        self.similar_acc = similar
        self.login_ = login
        self.password = password
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/button[2]'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/section/main/div/div/div[1]/div[2]/form/div/div[5]/button'))).click()
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]'))).click()
        self.driver.find_element(By.ID, 'email').send_keys(self.login_)
        self.driver.find_element(By.ID, 'pass').send_keys(self.password + Keys.ENTER)
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]'))).click()

    def find_followers(self):
        self.driver.get(f'https://www.instagram.com/{self.similar_acc}')
        self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a'))).click()

    def follow(self):
        people = self.wait.until(EC.element_to_be_clickable((By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div')))
        list_people = people.find_elements(By.LINK_TEXT, 'Подписаться')
        actions = ActionChains(self.driver)

        for person in list_people:
            print(person)
            # actions.move_to_element(person).perform()
            # print(person.find_element(By.ID, 'mount_0_0_pw').text)

        while True:
            pass
