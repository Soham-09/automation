
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime



webdriver = webdriver.Chrome("/home/soham/Downloads/chromedriver")#the path where chromedriver is present
sleep(2)
webdriver.get('https://www.instagram.com/accounts/login/?source=auth_switcher')
sleep(3)

username = webdriver.find_element_by_name('username')
username.send_keys('your_username')
password = webdriver.find_element_by_name('password')
password.send_keys('your_password')

button_login = webdriver.find_element_by_css_selector('div.Igw0E.IwRSH.eGOV_._4EzTm.bkEs3.CovQj.jKUp7.DhRcB')
button_login.click()
    

