from selenium import webdriver
import random
import time
from bs4 import BeautifulSoup
from myconfig import NAVER
import pyperclip
import pyautogui as gui

def load_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    return driver
def load_login_page():
    driver.implicitly_wait(3)
    driver.get('https://nid.naver.com/nidlogin.login')
def try_login():
    tag_id = driver.find_element_by_name('id')
    tag_pw = driver.find_element_by_name('pw')
    tag_id.clear()
    time.sleep(1)
    pyperclip.copy(myId)
    tag_id.click()
    gui.hotkey('command', 'v')
    time.sleep(1)
    pyperclip.copy(myPass)
    tag_pw.click()
    gui.hotkey('command', 'v')
    time.sleep(1)
    driver.find_element_by_xpath('//*[@id="log.login"]').click()
    time.sleep(3)
    driver.find_element_by_xpath('//*[@id="new.save"]').click()
    time.sleep(3)
def move_to_mailbox():
    driver.find_element_by_xpath('//*[@id="0_fol"]/span/a[1]').click()
    time.sleep(2)



def naver_stuff():
    load_login_page()
    try_login()
    request_webpage('https://mail.naver.com/')
    move_to_mailbox()
    # get_maillist_from_mailbox()

myId = NAVER["id"]
myPass = NAVER["password"]

# if __name__ = "__main__":
driver = load_driver()
naver_stuff()
prevent_close()
