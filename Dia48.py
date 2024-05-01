from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_option=webdriver.ChromeOptions()
chrome_option.add_experimental_option("detach", True)

driver=webdriver.Chrome(options=chrome_option)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

#price_page=driver.find_element(By.CLASS_NAME, value="andes-money-amount__fraction")
#searchbar=driver.find_element(By.NAME, value="as_word")
#button=driver.find_element(By.ID, value=":R15d3a6c4um:")
#delivery_form=driver.find_element(By.CSS_SELECTOR, value=".ui-pdp-action-modal a")
#print(f"This is the complete price ${price_page.text}")
#print(searchbar.get_attribute("placeholder"))
#link=driver.find_element(By.XPATH, value='/html/body/footer/div/div/div/nav/ul/li[1]/a')
#print(link.text)


#event_times=driver.find_elements(By.CSS_SELECTOR,value=".event-widget time")
#event_names=driver.find_elements(By.CSS_SELECTOR,value=".event-widget li a")
#events={}
#for n in range(len(event_times)):
 #   events[n]={
  #      "time":event_times[n].text,
   #     "name":event_names[n].text
    #}

#print(events )
#article_count=driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
#article_count.click()

#all_portals=driver.find_element(By.LINK_TEXT, value="Community portal")
#all_portals.click()
#search=driver.find_element(By.NAME, value="fName")
#search.send_keys("Cristian", Keys.TAB)

#search=driver.find_element(By.NAME, value="lName")
#search.send_keys("Ramos", Keys.TAB)

#search=driver.find_element(By.NAME, value="email")
#search.send_keys("ramosbarragan.cristian@gmail.com", Keys.TAB)

#button=driver.find_element(By.CLASS_NAME, value="btn-block")
#button.send_keys(Keys.ENTER)

cookie = driver.find_element(by=By.ID, value="cookie")

items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60*5  # 5 minutes

while True:
    cookie.click()

    if time.time() > timeout:

        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        money_element = driver.find_element(by=By.ID, value="money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()

        timeout = time.time() + 5

    if time.time() > five_min:
        cookie_per_s = driver.find_element(by=By.ID, value="cps").text
        print(cookie_per_s)
        break