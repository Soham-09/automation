from selenium import webdriver 


driver = webdriver.Chrome("/home/soham/Downloads/chromedriver") #the path where chromedriver is present so that python can find it
driver.get('https://www.facebook.com/') 
 
 

username_box = driver.find_element_by_id('email') 
username_box.send_keys('user_emai_id') 
 

password_box = driver.find_element_by_id('pass') 
password_box.send_keys('user_password') 
 

login_box = driver.find_element_by_id('loginbutton') 
login_box.click() 

 


