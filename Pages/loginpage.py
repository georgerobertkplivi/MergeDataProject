from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class LoginPage:

    # Login Page Locators
    textbox_Email_id = "email"
    textbox_Password_name = "password"
    btn_login_xpath = "//button[@class='btn btn-lg btn-primary']"


    def __init__(self, driver):
        self.driver = driver

    def checkHomePageUrl(self):
        browser = self.driver
        url = browser.current_url
        return url

    def setEmail(self,email):
        browser = self.driver
        browser.find_element(By.ID, self.textbox_Email_id).clear()
        browser.find_element(By.ID, self.textbox_Email_id).send_keys(email)


    def setPassword(self, password):
        browser = self.driver
        browser.find_element(By.NAME, self.textbox_Password_name).clear()
        browser.find_element(By.NAME, self.textbox_Password_name).send_keys(password)

    def clickLoginButton(self):
        browser = self.driver
        browser.find_element(By.XPATH, self.btn_login_xpath).click()

