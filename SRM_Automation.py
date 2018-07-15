from selenium import webdriver
import time
driver=webdriver.Chrome('C:\\Chrome driver\\chromedriver.exe')
driver.maximize_window()
driver.get('https://academia.srmuniv.ac.in/')
driver.switch_to.frame(driver.find_element_by_tag_name('iframe'))
driver.implicitly_wait(10)
driver.find_element_by_name('username').send_keys('varungopal_kg@srmuniv.edu.in')
driver.find_element_by_name('password').send_keys('VGvarun@97')
a = driver.find_element_by_xpath("//*[@id='signinForm']/div[5]/input")
a.click()
time.sleep(20)
driver.quit()
