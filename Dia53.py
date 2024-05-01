from bs4 import BeautifulSoup
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


Headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
    "Accept-Language":"es-419,es;q=0.8"
}

response=requests.get("https://appbrewery.github.io/Zillow-Clone/", headers=Headers)
data=response.text
soup=BeautifulSoup(data, "html.parser")

all_links=soup.select(".StyledPropertyCardDataWrapper a")
href=[]
for link in all_links:
    href.append(link["href"])


all_address=soup.select(".StyledPropertyCardDataArea-anchor address")
addresses = [address.get_text().replace(" | ", " ").strip() for address in all_address]

all_price_elements=soup.select(".PropertyCardWrapper span")
all_prices = [price.get_text().replace("/mo", "").split("+")[0] for price in all_price_elements if "$" in price.text]



chrome_options=webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver=webdriver.Chrome(options=chrome_options)

for n in range(len(all_links)):
    driver.get("https://docs.google.com/forms/d/e/1FAIpQLSdnVZnSM0JgrLfdeZax8r8mquy9eLQgo8vsV-9ynT9rfHtUGQ/viewform?usp=sf_link")
    time.sleep(2)

    # Use the xpath to select the "short answer" fields in your Google Form. 
    # Note, your xpath might be different if you created a different form.
    address = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit_button = driver.find_element(by=By.XPATH, 
                        value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    
    address.send_keys(addresses[n])
    price.send_keys(all_prices[n])
    link.send_keys(all_links[n])
    submit_button.click()