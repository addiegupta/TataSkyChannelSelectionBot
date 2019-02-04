import sys

sys.path.append('..')
from selenium import webdriver
import pandas as pd
import time
from selenium.webdriver.common.keys import Keys
from optparse import OptionParser


def parse_excel_sheet(file_loc):
    df = pd.read_excel(file_loc, index_col=None, na_values=['NA'], usecols="A")
    channels = []
    for index, row in df.iterrows():
        if type(row[0]) is not float:
            channels.append(row[0])

    return channels


def start_selecting_channels(mobile_number, file_name):

    driver = webdriver.Chrome("Drivers\chromedriver.exe")
    driver.set_page_load_timeout(10)

    print("10 second timeout")

    link = "https://packselection.tatasky.com/PRRedirect/PRWebMQ"
    driver.get(link)

    driver.find_element_by_name("rmn").send_keys(mobile_number)
    driver.find_element_by_css_selector("button[type='submit']").send_keys(Keys.ENTER)
    time.sleep(2)
    driver.find_element_by_xpath("//*[@id='placeHold']").click()
    print("20 seconds to enter OTP")
    time.sleep(20)

    channels = parse_excel_sheet(file_name)

    driver.find_element_by_xpath("/html/body/section/div/div/div/div[3]/div/h5/a/span[1]").click()
    time.sleep(5)
    driver.find_element_by_xpath("//a[@href='#collapse1']").click()
    time.sleep(2)
    driver.find_element_by_xpath("//a[@href='#collapse3']").click()

    for channel in channels:
        # Search channel
        driver.find_element_by_xpath("//*[@id='imaginary_container']/div/input").send_keys(channel)

        # Click checkbox
        try:
            driver.find_element_by_xpath(
                "//span[contains(text(),'" + channel + "')]/../input[@class='checkboxDefault alcTskyBouquetCheckbox allPacksCheckboxes']").click()
        except:
            print(channel + " not found")
        time.sleep(2)

        # Clear searchbox
        driver.find_element_by_xpath("//*[@id='imaginary_container']/div/input").clear()

    driver.find_element_by_xpath("/html/body/section/div[1]/div/p[1]/button").click()
    time.sleep(4)

    time.sleep(100000)
    driver.quit()


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
    file_name = args[1]

    start_selecting_channels(mobile_number, file_name)


if __name__ == '__main__':
    sys.exit(main())
