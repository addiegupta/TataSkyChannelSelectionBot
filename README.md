# Tata Sky Channel Selection Bot

This Python script selects the channels from a Spreadsheet (.xlsx) and selects them on Tata Sky's new channel selection portal.

##Usage

-Clone the repository/ Download ZIP

-In the *channels.xlsx" file, remove the *#* from the channels that you want and save it

OR

Create an xlsx file having required channel names in column B.

-Open a terminal in the files location and run

`python select_channels.py "<registered-mobile-number>" "<xlsx-file-name>"`

- Enter OTP when required

- Wait for the channels to get selected

- Finalise changes


<table>
        <tr>
<td><img src = "https://user-images.githubusercontent.com/22665789/52260588-983e8c00-294c-11e9-94cd-bb2467d5f511.gif" height = "322" width="600"></td>
    </tr>
</table>


##Libraries Used

[Selenium: Browser Automation](https://www.seleniumhq.org/)

[Pandas: Python Data Analysis Library](https://pandas.pydata.org/)