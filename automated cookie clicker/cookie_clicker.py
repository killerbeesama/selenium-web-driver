from selenium import webdriver
import time

driver = webdriver.Chrome("<your path>")
driver.get("http://orteil.dashnet.org/experiments/cookie/")


def update_sec():
    sec = time.time() + 5
    return sec


cookie = driver.find_element_by_id("cookie")
second_ahead = update_sec()
minute_ahead = time.time() + 60*5 # 5min

while True:
    current_time = time.time()
    if current_time >= minute_ahead:
        cookie_per_sec = driver.find_element_by_id("cps").text
        print(cookie_per_sec)
        driver.quit()
        break
    elif current_time > second_ahead:
        money_count = driver.find_element_by_css_selector("div #money")
        money = int(money_count.text.replace(",",""))
        cookie_store = driver.find_elements_by_css_selector("#store b")
        item_price = [int(i.text.split("-")[1].replace(",", "")) for i in cookie_store[:-1:1]]
        highest = 0
        for price in item_price:
            if money > price:
                highest = price
        try:
            cookie_store[item_price.index(highest)].click()
        except ValueError:
            pass
        finally:
            second_ahead = update_sec()
    else:
        cookie.click()




