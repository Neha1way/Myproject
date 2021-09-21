import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import pytest
import pyautogui
from fpdf import FPDF

global driver
@pytest.fixture()
def test_setup():
    global driver
    driver=webdriver.Chrome(executable_path="E:\MyFirstProject\Chrome\chromedriver.exe")
    driver.maximize_window()
    driver.implicitly_wait(20)
    email = "neha@1wayit.com"
    password = "neha786"
    driver.get("https://oenostage.1wayit.com/")
    driver.find_element_by_name("email").send_keys(email)
    driver.find_element_by_name("password").send_keys(password)
    submit = driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[1]/div[2]/form/div[2]/button")
    submit.click()
    time.sleep(5)

# Get title of each module
# def test_title(test_setup):
#     print(driver.title)
#     leads = "Oeno"
#     if leads in driver.title:
#         print ("exact title")
#     else:
#         print("title not matched")

#Clicked on each module of side bar and taking screenshot of each module
def test_clickeach_module(test_setup):
    j=1
    for i in range(1,17):
        print (i)
        time.sleep(1)
        driver.find_element_by_xpath("//div[@id='sidebar']/ul/li["+str(i)+"]/a").click()
        time.sleep(3)
# Taking screenshot
        myScreenshot = pyautogui.screenshot()
        myScreenshot.save(r'E:/Python Neha workspace/Screenshot/Screenshot'+str(i)+'.png')
# # To create pdf file
#         from fpdf import FPDF
#         pdf = FPDF()
#         pdf.add_page()
#         pdf.set_font('Arial', 14)
#         pdf.cell(200, 10,'Welcome to PythonGuides')
#         pdf.output('python.pdf')

#To click on sub modules incorporated by main modules
        try:
            driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[" + str(i) + "]/span").click()
        except Exception:
            try:
                driver.find_element_by_xpath("//*[@id='sub-menu']/ul/ul["+j+"]").click()
                time.sleep(3)
            except Exception:
                print("Sub module found" )
        j=j+1
print("Done")
#
# # Creating a new lead
# def test_new_lead(test_setup):
#     driver.find_element_by_xpath("//div[@id='sidebar']/ul/li[2]/a").click()
#     driver.find_element_by_xpath("//div[@class='col-lg pl-0']/div[1]/a[2]").click()
#     element = driver.find_element_by_name("cat_id")
#     drp = Select(element)
#     drp.select_by_visible_text('Test Category')
#     time.sleep(2)
#     firstname = "Sushant"
#     lastname = "Test"
#     email = "test786@yopmail.com"
#     phone = "9876789999"
#     work_email = "workemail@yopmail.com"
#     work_phone = "8976546789"
#     investment = "5000"
#     addressline1 = "C-204 Atrium Tower"
#     addressline2 = "Near world tech tower"
#     city = "Mohali"
#     county = "Zapp"
#     postalcode = "MNB567"
#     driver.find_element_by_name("firstname").send_keys(firstname)
#     driver.find_element_by_name("lastname").send_keys(lastname)
#     driver.find_element_by_name("email").send_keys(email)
#     driver.find_element_by_id("phone").send_keys(phone)
#     driver.find_element_by_name("work_email").send_keys(work_email)
#     driver.find_element_by_name("work_phone").send_keys(work_phone)
#     #driver.find_element_by_id("datepicker").click()
#     driver.find_element_by_name("investment_level").send_keys(investment)
#     driver.find_element_by_name("address_line1").send_keys(addressline1)
#     driver.find_element_by_name("address_line2").send_keys(addressline2)
#     element=driver.find_element_by_name("country")
#     drp=Select (element)
#     drp.select_by_visible_text('Argentina')
#     driver.find_element_by_name("city").send_keys(city)
#     driver.find_element_by_name("county").send_keys(county)
#     driver.find_element_by_name("postal_code").send_keys(postalcode)
#     driver.find_element_by_xpath("//div[@class='btn-section mt-60']/button").click()
#     driver.find_element_by_xpath("//div[@id='KYC']/div[5]/button").click()


