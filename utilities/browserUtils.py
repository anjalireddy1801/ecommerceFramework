from selenium import webdriver

class browserUtils:

    def __init__(self,driver):
        self.driver=driver
        

    def get_title(self):
        print(self.driver.title)