from selenium import webdriver

driver = webdriver.Chrome("<your path>")
driver.get("https://en.wikipedia.org/wiki/Main_Page")
article_count = driver.find_element_by_css_selector("#articlecount a").text
print(article_count)
driver.quit()

