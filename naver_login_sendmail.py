from selenium import webdriver
import time
from bs4 import BeautifulSoup
from myconfig import NAVER
import pyperclip
import pyautogui as gui
import openpyxl as xl

def load_driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome('/usr/local/bin/chromedriver')
    return driver
def load_login_page():
    driver.implicitly_wait(2)
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
    time.sleep(2)
def move_to_mailbox():
    driver.find_element_by_xpath('//*[@id="0_fol"]/span/a[1]').click()
    time.sleep(1)
def go_to_mailsend():
    driver.find_element_by_xpath('//*[@id="nav_snb"]/div[1]/a[1]/strong/span').click()
    time.sleep(1)


def send_mail():
    wb = xl.load_workbook('/usr/local/bin/주문내역.xlsx')
    ws = wb.active
    lst = []
    for r in ws.rows:
        if r[0].value is None: #빈 셀 건너 뛰기
            continue
        lst.append([]) # 행의 데이터 추가.
        for c in r:
            lst[-1].append(c.value)
        print(lst[-1])
    lst.pop(0)
    for i in lst:
        pyperclip.copy(i[-1])
        gui.hotkey('command', 'v')
        time.sleep(1)
        gui.hotkey('tab')
        gui.hotkey('tab')
        pyperclip.copy('[동호 마켓] {}님의 주문내역을 안내드립니다'.format(i[1]))
        gui.hotkey('command', 'v')
        time.sleep(1)
        #파일첨부
        # driver.find_element_by_xpath('//*[@id="AddButton_html5"]').send_keys('/usr/local/bin/주문내역.xlsx')
        # time.sleep(2)
        gui.hotkey('tab')
        pyperclip.copy('''
        안녕하세. {}님. 동호 마켓입니다.
        {}-{}-{}에 주문하신 제품에 대해 안내드립니다.

        제품명 : {}
        금액 : {:,}

        주문해주셔서 감사합니다.
        '''.format(i[1], i[0].year, i[0].month, i[0].day, i[2], i[3]))
        gui.hotkey('command', 'v')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="sendBtn"]').click()

def request_webpage():
    driver.get('https://mail.naver.com/')
    time.sleep(1)

def naver_stuff():
    load_login_page()
    try_login()
    request_webpage()
    go_to_mailsend()
    send_mail()

myId = NAVER["id"]
myPass = NAVER["password"]

# if __name__ = "__main__":
driver = load_driver()
naver_stuff()
prevent_close()
