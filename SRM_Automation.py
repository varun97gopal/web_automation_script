#Varun code
from selenium import webdriver
import time
driver = webdriver.Chrome('C:\\# your root directory')
driver.maximize_window()
driver.get('https://academia.srmuniv.ac.in')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.implicitly_wait(10)
driver.find_element_by_name('username').send_keys('#your srmID')
driver.find_element_by_name('password').send_keys('#your password')
a = find_element_by_xpath("//*[@id='signinForm']/div[5]/input")
c.click()
time.sleep(5)
driver.quit()
#Varun code
