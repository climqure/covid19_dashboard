from selenium import webdriver

driver = webdriver.Firefox()
driver.get('https://covid19.who.int/')

button = driver.find_element_by_xpath(
    '/html/body/div[1]/div/div[2]/div[1]/div/div[5]/div/button/div/span')
button.click()
