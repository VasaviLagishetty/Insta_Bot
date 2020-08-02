from selenium.webdriver.common.keys import Keys
import time
from utility_methods.utility_methods import *
import urllib.request
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


class InstBot:

    def __init__(self,username,password):
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome()

        self.login()
        self.follow()
        
    def login(self):

        self.driver.get('https://www.instagram.com')

        wait = WebDriverWait(self.driver, 10)

        second_page_flag = wait.until(EC.presence_of_element_located(
            (By.CLASS_NAME, "KPnG0")))  # util login page appear

        username_input = self.driver.find_element_by_name("username")

        password_input = self.driver.find_element_by_name('password')

        ActionChains(self.driver)\
            .move_to_element(username_input).click()\
            .send_keys(self.username)\
            .move_to_element(password_input).click()\
            .send_keys(self.password)\
            .perform()

        button = self.driver.find_element_by_class_name("L3NKy") 
        
        button.click()

        time.sleep(2)

    def find_button(self, button_text):

        buttons = self.driver.find_element_by_xpath("//*[text()='{}']".format(button_text))

        return buttons

    def follow(self):

        self.driver.get('https://www.instagram.com/'+'man_with_3_eyes')

        try:
            follow_buttons = self.find_button('Follow')
            follow_buttons.click()
        except:
            pass

        time.sleep(5)

    def like_save_comment(self,post_url,post_comment):

        self.driver.get(post_url)

        like_save_post = self.driver.find_elements_by_class_name("_8-yf5") 

        
        print(like_save_post)

        for i in like_save_post:
            print(i.get_attribute('aria-label'))

        time.sleep(2)

        like_save_post[1].click() #like_post

        time.sleep(2)

        like_save_post[5].click() #save_post

        time.sleep(2)

        if post_comment != None:

            comment = self.driver.find_element_by_class_name("Ypffh")

            print(comment)

            ActionChains(self.driver)\
                .move_to_element(comment).click()\
                .send_keys(post_comment)\
                .perform()

            time.sleep(2)

            post_comment_button = self.find_button('Post')

            post_comment_button.click()

            time.sleep(5)
        

    def close(self):

        self.driver.quit()

               
if __name__ == '__main__':

    bot = InstBot('dragonperu@protonmail.com','Dsragonperu@123')

    posts = [('https://www.instagram.com/p/BVhd7bLlhhC/',None)]
    
    
    for url_comment in posts:

        bot.like_save_comment(url_comment[0],url_comment[1])

    bot.close()