from selenium import webdriver
from selenium.webdriver.common.by import By
from pageObjects.shopPage import shopPage
from utilities.browserUtils import browserUtils


class loginPage(browserUtils):
    def __init__(self,driver): #INITIALIZING DRIVER AND LOCATORS
        super().__init__(driver) #initializing/activating driver in parent class
        self.driver=driver
        self.username=(By.ID,"username")
        self.password=(By.ID,"password")
        self.signIn=(By.ID,"signInBtn")
     


    def login(self,username_input,password_input): #ACTIONS IN THE PAGE
        self.driver.find_element(*self.username).send_keys(username_input)
        self.driver.find_element(*self.password).send_keys(password_input)
        self.driver.find_element(*self.signIn).click()
        # shop_obj=shopPage(self.driver)
        # return shop_obj