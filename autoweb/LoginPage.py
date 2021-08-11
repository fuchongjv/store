from selenium.webdriver.common.by import By
import time


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    def login(self, username, pwd):
        self.driver.get("http://192.168.10.228/login?redirect=%2Findex")

        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[1]/div/div/input").send_keys(username)

        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[2]/div/div/input").send_keys(pwd)

        self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[4]/div/button").click()

        time.sleep(0.2)

    def get_login_success(self):
        return self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[3]/div/div[3]").text

    def get_login_pwd_error(self):
        return self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div[3]/div/div[3]").text
