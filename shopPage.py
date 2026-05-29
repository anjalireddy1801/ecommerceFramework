from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from pageObjects.confPage import confPage
from utilities.browserUtils import browserUtils

class shopPage(browserUtils):
    def __init__(self,driver):
        super().__init__(driver)
        self.driver=driver
        self.shop_link=(By.XPATH,"//a[text()='Shop']")
        self.products=(By.XPATH,"//div[@class='card h-100']")
        self.cart=(By.XPATH,"//div[@id='navbarResponsive']/ul/li/a")


    def addtocart(self,product_user):
        
        self.driver.find_element(*self.shop_link).click()

        

        product_list=self.driver.find_elements(*self.products)

        #adding product to cart

        for product in product_list:
            product_name=product.find_element(By.XPATH,"div/h4/a").text #no need to declare in init since child loactors
            if product_name == product_user:
                product.find_element(By.XPATH,"div/button").click() #no need to declare in init since child loactors



      


    def gotocart(self):
        #clicking on cart
        time.sleep(4)
        self.driver.find_element(*self.cart).click()
        checkout_obj=confPage(self.driver)
        # return checkout_obj

        

        

        