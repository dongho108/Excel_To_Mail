import openpyxl as xl
import pyperclip as clp
import pyautogui as gui
import time

wb = xl.load_workbook('주문내역.xlsx')
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
    x, y = gui.locateCenterOnScreen('03_01.PNG')
    # gui.click(x, y)
    # time.sleep(1)
    clp.copy(i[-1])
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    gui.hotkey('tab')
    gui.hotkey('tab')
    clp.copy('[동호 마켓] {}님의 주문내역을 안내드립니다.'.format(i[1]))
    gui.hotkey('ctrl', 'v')
    time.sleep(1)
    gui.hotkey('tab')

    clp.copy('''
    안녕하세. {}님. 동호 마켓입니다.
    {}-{}-{}에 주문하신 제품에 대해 안내드립니다.

    제품명 : {}
    금액 : {:,}

    주문해주셔서 감사합니다.
    '''.format(i[1], i[0].year, i[0].month, i[0].day, i[2], i[3]))
    gui.hotkey('ctrl', 'v')
    time.sleep(1)

    x, y = gui.locateCenterOnScreen('03_02.PNG')
    gui.click(x, y)
    time.sleep(20)
