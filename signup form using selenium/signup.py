from selenium import webdriver

driver = webdriver.Chrome("<your path>")
driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element_by_name("fName")
first_name.send_keys("hello")
last_name = driver.find_element_by_name("lName")
last_name.send_keys("world")
email = driver.find_element_by_name("email")
email.send_keys("helloworld@gmail.com")
button = driver.find_element_by_tag_name('button')
button.click()
