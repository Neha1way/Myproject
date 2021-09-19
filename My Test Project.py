import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
global driver
@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="E:\MyFirstProject\Chrome\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(20)
# Login into system with user credentials
def test_login(test_setup):
    email = "neha@1wayit.com"
    password = "neha786"
    driver.get("https://oenostage.1wayit.com/")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    submit = driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[1]/div[2]/form/div[2]/button")
    submit.click()
    time.sleep(5)
# Get title of each module
#print(driver.title)
#leads = "Oeno"
#if leads in driver.title:
 #   print ("exact title")
#else:
   # print("title not matched")
# Clicked on each module of side bar
def clickeach_module(test_setup):
    time.sleep(5)
    j=1
    for i in range(1,17):
        print (i)
        time.sleep(3)
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li["+str(i)+"]/a").click()
        time.sleep(2)
        try:
            driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[" + str(i) + "]/span").click()
        except Exception:
            try:
                driver.find_element_by_xpath("//*[@id='sub-menu']/ul/ul["+j+"]").click()
                time.sleep(3)
            except Exception:
                print("ffff")
        j=j+1
print("Done")
# Creating a new lead
def new_lead(test_setup):
    driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/a").click()
    driver.find_element_by_xpath("//div[@class='col-lg pl-0']/div[1]/a[2]").click()
    element=driver.find_element_by_xpath("//div[@class='form-group d-flex']/select").click()
    drp=Select(element)
    drp.select_by_visible_text('Test Category')
    firstname = "Sushant"
    lastname ="Test"
    driver.find_element_by_name("firstname").send_keys(firstname)
    driver.find_element_by_name("lastname").send_keys(lastname)



