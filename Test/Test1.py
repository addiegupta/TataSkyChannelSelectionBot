import sys
sys.path.append('..')
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from optparse import OptionParser


def main():

    usage = """
    %prog mobileNumber ExcelSheet.xlsx
    """

    parser = OptionParser(usage=usage)

    (cmdlineOptions, args) = parser.parse_args()
    if len(args) < 2:
        parser.print_help()
        sys.exit(1)

    mobile_number = args[0]
    excel_file = args[1]

    driver = webdriver.Chrome("..\Drivers\chromedriver.exe")

    driver.set_page_load_timeout(10)
    link = "https://packselection.tatasky.com/PRRedirect/PRWebMQ"
    driver.get(link)

    # mobNumber = "insertNumber"

    driver.find_element_by_name("rmn").send_keys(mobNumber)
    driver.find_element_by_css_selector("button[type='submit']").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='placeHold']").click()
    time.sleep(20)
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
        if type(row[0]) is float:
            continue
        #Search channel
        driver.find_element_by_xpath("//*[@id='imaginary_container']/div/input").send_keys(row[0])

        #Click checkbox
        try:
            channel_element = driver.find_element_by_xpath("//span[contains(text(),'"+row[0]+"')]/../input[@class='checkboxDefault alcTskyBouquetCheckbox allPacksCheckboxes']").click()
        except:
            print(row[0]+" not found")
        time.sleep(2)

        #Clear searchbox
        driver.find_element_by_xpath("//*[@id='imaginary_container']/div/input").clear()

    driver.find_element_by_xpath("/html/body/section/div[1]/div/p[1]/button").click()
    time.sleep(4)

    time.sleep(100000)
    driver.quit()

if __name__ == '__main__':
    sys.exit(main())
