from selenium import webdriver
import time
import os 
try:
 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)
    input1 = browser.find_element_by_xpath("//input[@placeholder='Enter first name']")
    input1.send_keys("Ivan")
    input2 = browser.find_element_by_xpath("//input[@placeholder='Enter last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element_by_xpath("//input[@placeholder='Enter email']")
    input3.send_keys("Email")


    current_dir = os.path.abspath(os.path.dirname(__file__))   
    file_path = os.path.join(current_dir, 'file.txt')          
    input4 = browser.find_element_by_id('file')
    input4.send_keys(file_path)
    
    button = browser.find_element_by_css_selector(".btn.btn-primary")
    button.click()
    
finally:
    time.sleep(10)
    browser.quit()