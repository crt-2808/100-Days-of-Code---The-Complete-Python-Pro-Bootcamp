from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
import dotenv
import time
import os

dotenv.load_dotenv()

SIMILAR_ACCOUNT = "foforrolgaming"
USERNAME = os.getenv("Instagram_user")
PASSWORD = os.getenv("Instagram_pass")

class InstaFollower:
    def __init__(self):
        chromeOptions=webdriver.ChromeOptions()
        chromeOptions.add_experimental_option("detach", True)
        self.driver=webdriver.Chrome(options=chromeOptions)
        
    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        time.sleep(4.5)
        
        username_input=self.driver.find_element(By.NAME, value="username")
        password_input=self.driver.find_element(By.NAME, value="password")

        username_input.send_keys(USERNAME)
        password_input.send_keys(PASSWORD)

        time.sleep(2.5)
        password_input.send_keys(Keys.ENTER)

        time.sleep(5)

        save_login_prompt=self.driver.find_element(By.XPATH, value='//*[@role="button"]')
        if save_login_prompt:
            save_login_prompt.click()

        time.sleep(3.7)

        notifications_prompt = self.driver.find_element(By.XPATH, value="// button[contains(text(), 'Ahora no')]")
        if notifications_prompt:
            notifications_prompt.click()

    def find_followers(self):
        time.sleep(5)
        # Show followers of the selected account. 
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}/followers")

        time.sleep(5.2)
        # The xpath of the modal that shows the followers will change over time. Update yours accordingly.
        modal_xpath = "/html/body/div[6]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]"
        modal = self.driver.find_element(by=By.XPATH, value=modal_xpath)
        for i in range(2):
            # In this case we're executing some Javascript, that's what the execute_script() method does.
            # The method can accept the script as well as an HTML element.
            # The modal in this case, becomes the arguments[0] in the script.
            # Then we're using Javascript to say: "scroll the top of the modal (popup) element by the height of the modal (popup)"
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            time.sleep(2)
    
    def follow(self):
        # Check and update the (CSS) Selector for the "Follow" buttons as required.
        all_buttons = self.driver.find_elements(By.XPATH, value="//div[contains(text(), 'Seguir')]")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1.5)
            # Clicking button for someone who is already being followed will trigger dialog to Unfollow/Cancel
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(by=By.XPATH, value="//button[contains(text(), 'Cancel')]")
                cancel_button.click()



bot=InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
