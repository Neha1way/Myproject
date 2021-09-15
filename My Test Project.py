import time

from selenium import webdriver

driver=webdriver.Chrome(executable_path="E:\MyFirstProject\Chrome\chromedriver.exe")

driver.maximize_window()
driver.implicitly_wait(20)
#time.sleep(10)
email = "neha@1wayit.com"
password = "neha786"
driver.get("https://oenostage.1wayit.com/")
driver.find_element_by_name("email").send_keys(email)
driver.find_element_by_name("password").send_keys(password)
submit = driver.find_element_by_xpath("/html/body/div[1]/main/div/div/div[1]/div[2]/form/div[2]/button")
submit.click()

# Get title of each module
print(driver.title)
leads = "Oeno"
if leads in driver.title:
    print ("exact title")
else:
    print("title not matched")
driver.close()
