from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
from utilities.browserUtils import browserUtils

class confPage(browserUtils):

    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.checkout_button=(By.XPATH,"//button[@class='btn btn-success']")

        self.country=(By.ID,"country")
        self.countries=(By.CLASS_NAME,"suggestions")
        self.country_dropdown=(By.XPATH,"//ul/li/a[text()='India']")
        self.checkbox=(By.XPATH,"//div/label[@for='checkbox2']")
        self.submit=(By.XPATH,"//input[@type='submit']")
        self.message=(By.XPATH,"//div[@class='alert alert-success alert-dismissible']")
        pass


    def checkout(self):
        #checkout button
        self.driver.find_element(*self.checkout_button).click()


    def address(self,country_name):
        self.driver.find_element(*self.country).send_keys(country_name)

        wait=WebDriverWait(self.driver,10)

        wait.until(expected_conditions.visibility_of_element_located((self.countries)))

        self.driver.find_element(*self.country_dropdown).click()

        self.driver.find_element(*self.checkbox).click()

        self.driver.find_element(*self.submit).click()


    def validate(self):

        message=self.driver.find_element(*self.message).text

        print(message)

        assert 'Success' in message


