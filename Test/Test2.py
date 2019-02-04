from selenium import webdriver
import time

driver = webdriver.Chrome("D:\Aditya\Desktop\Tata Sky Select\Drivers\chromedriver.exe")


driver.set_page_load_timeout(30)
link = "https://www.checkli.com/checklists/view/5c580a969559d"
driver.get(link)
time.sleep(4)

parent_element = driver.find_element_by_xpath("//p[text()='world']/../label[@class='form-label ng-scope']")
print("FOUND ")
parent_element.click()

time.sleep(10)
driver.quit()
