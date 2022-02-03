from selenium import webdriver

driver = webdriver.Chrome("<your path>")
driver.get("https://www.python.org/")
event_web_data = driver.find_elements_by_css_selector(".event-widget li a")
event_date_web_data = driver.find_elements_by_css_selector(".event-widget li time")
event_date = [event_date_web_data[i].text for i in range(len(event_date_web_data))]
event_name = [event_web_data[i].text for i in range(len(event_web_data))]
event = {}
for i in range(len(event_date)):
    event[i] = {'date': event_date[i], 'name': event_name[i]}
print(event)

driver.quit()