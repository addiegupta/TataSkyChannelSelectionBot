from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\Aditya\Desktop\Tata Sky Select\Drivers\chromedriver.exe")


driver.set_page_load_timeout(10)
link = "https://packselection.tatasky.com/PRRedirect/PRWebMQ"
driver.get(link)
mobNumber = "insert_number_here"
driver.find_element_by_name("rmn").send_keys(mobNumber)
driver.find_element_by_css_selector("button[type='submit']").send_keys(Keys.ENTER)
time.sleep(20)
driver.find_element_by_xpath("/html/body/section/div/div/div/div[3]/div/h5/a/span[1]").click()
time.sleep(10)
driver.find_element_by_xpath("//a[@href='#collapse3']").click()


driver.quit()
