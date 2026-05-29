from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.ui import WebDriverWait
import time
from pageObjects.loginPage import loginPage
from pageObjects.shopPage import shopPage
from pageObjects.confPage import confPage
import json
import pytest

test_data_path = r'testData/test_e2e.json'
with open(test_data_path) as f:
    test_data=json.load(f)
    test_data_list=test_data["data"]



# @pytest.mark.smoke
@pytest.mark.parametrize("test_data_list_items",test_data_list)
def test_e2e(browser_instance,test_data_list_items):
        
    driver=browser_instance

    driver.get('https://rahulshettyacademy.com/loginpagePractise/')
    driver.maximize_window()

    login_obj=loginPage(driver)
    login_obj.get_title() #inc=vokes parent class via child class in Page object class
    login_obj.login(test_data_list_items["username_input"],test_data_list_items["password_input"])
    #shop_obj= login_obj.login(test_data_list_items["username_input"],test_data_list_items["password_input"])

    shop_obj=shopPage(driver)
    shop_obj.get_title()
    shop_obj.addtocart(test_data_list_items["product_user"])
    shop_obj.gotocart()
    # checkout_obj= shop_obj.gotocart()
    #-----------------------
    checkout_obj=confPage(driver)
    checkout_obj.get_title()
    checkout_obj.checkout()
    checkout_obj.address('ind')
    checkout_obj.validate()


    




    

   

  









