from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome("D:\Aditya\Desktop\Tata Sky Select\Drivers\chromedriver.exe")


driver.set_page_load_timeout(10)
link = "https://packselection.tatasky.com/PRRedirect/PRWebMQ"
driver.get(link)
mobNumber = "insertNumber"
driver.find_element_by_name("rmn").send_keys(mobNumber)
driver.find_element_by_css_selector("button[type='submit']").send_keys(Keys.ENTER)
time.sleep(2)
driver.find_element_by_xpath("//*[@id='placeHold']").click()
time.sleep(30)
driver.find_element_by_xpath("/html/body/section/div/div/div/div[3]/div/h5/a/span[1]").click()
time.sleep(5)
driver.find_element_by_xpath("//a[@href='#collapse1']").click()
time.sleep(2)
driver.find_element_by_xpath("//a[@href='#collapse3']").click()

file_loc = "D:\Aditya\Desktop\Tata Sky Select\Tata Sky Channels List.xlsx"
df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="B")

# print(df)
channels = []
for index, row in df.iterrows():

    channels.append(row[0])

#Click checkbox
# driver.find_element_by_xpath("//*[@id='imaginary_container']/div/input").send_keys(channels[0])
# channel_element = driver.find_element_by_css_selector("//span[.='"+channels[0]+"']")

channel_element = driver.find_element_by_xpath("//span[contains(text(),'"+channels[0]+"')]/../input[@class='checkboxDefault alcTskyBouquetCheckbox allPacksCheckboxes']").click()
# channel_element_parent = channel_element.find_element_by_xpath("..")
# channel_element_parent.find_element_by_xpath("//input[@class='checkboxDefault alcTskyBouquetCheckbox allPacksCheckboxes']").send_keys(Keys.ENTER)




# channel_element_parent = channel_element.find_element_by_xpath("..")
# channel_element_parent.find_element_by_xpath("//input[@type='checkbox'").click()

# for channel in channels:
#     print(channel)
#
time.sleep(100000)
driver.quit()
