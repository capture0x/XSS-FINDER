import random
from time import sleep
from selenium import webdriver
from selenium.common.exceptions import UnexpectedAlertPresentException
import sys
from selenium.webdriver.chrome.options import Options


class colors:
    OKBLUE = '\033[94m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CBLACK = '\33[30m'
    CRED = '\33[31m'
    CGREEN = '\33[32m'
    CYELLOW = '\33[33m'
    CBLUE = '\33[34m'
    CVIOLET = '\33[35m'
    CBEIGE = '\33[36m'
    CWHITE = '\33[37m'


color_random = [colors.CBLUE, colors.CVIOLET, colors.CWHITE, colors.OKBLUE, colors.CGREEN, colors.WARNING,
                colors.CRED, colors.CBEIGE]
random.shuffle(color_random)


def entryy():
    x = color_random[0] + """
       ⣿⣿⣿⣿⣿⣿⣿⣉⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣷⡈⢿⣿⣿⣿⣿⣿⣿⡏⣹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣍⡙⢿⣿⣦⡙⠻⣿⣿⣿⡿⠁⣾⣿⣿⣿⡿⢿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⣿⣦⡉⠛⠓⠢⡈⢿⡿⠁⣸⣿⡿⠿⢋⣴⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣯⣍⣙⡋⠠⠄⠄⠄⠄⠁⠘⠁⠄⠴⠚⠻⢿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣿⣿⡿⠿⢏⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠄⠹⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⣿⣿⣧⡴⠖⠒⠄⠁⠄⢀⠄⠄⠄⡀⠄⠄⠄⠄⠄⠄⣠⣿⣿⣿⣿⣿⣿
       ⣿⣿⣿⠿⠟⣩⣴⣶⣿⣿⣶⡞⠉⣠⣇⠄⣿⣶⣦⣄⡀⠲⢿⣿⣿⣿⣿⣿⣿⣿
       ⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⡿⢠⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣶⣌⠻⠿⣿⣿⣿⣿ <<   XSS FINDER TOOL    >>
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢡⣿⣿⣿⡏⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿ <<  CODED BY TMRSWRR    >>
       ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣸⣿⣿⣿⣷⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿ <<  INSTAGRAM==>tmrswrr >>
\n"""
    for c in x:
        print(c, end='')
        sys.stdout.flush()
        sleep(0.0045)
    oo = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in oo:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)

    tt = " " * 6 + "░⣿" + " " * 18 + "WELCOME TO XSS FINDER TOOL" + " " * 11 + "░⣿" + "\n\n"
    for c in tt:
        print(colors.CWHITE + c, end='')
        sys.stdout.flush()
        sleep(0.0065)
    xx = " " * 6 + 29 * "░⣿" + "\n\n"
    for c in xx:
        print(colors.CGREEN + c, end='')
        sys.stdout.flush()
        sleep(0.0065)


def xssInj(c):
    print("Trying payloads list, PLease wait...")
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(executable_path="/usr/bin/chromedriver", options=chrome_options)
    browser.maximize_window()
    count = 0
    with open("myfile.txt", "r", encoding="UTF-8") as file:
        a = file.readlines()
        try:
            while count < len(a):
                browser.get(c + a[count])
                sleep(random.randint(1, 3))
                count += 1
                if count == len(a):
                    browser.close()
        except UnexpectedAlertPresentException:
            print(colors.CRED + "Successful Payload==>", a[count - 1])
            print("Url==>" + c + a[count - 1])
            sleep(5)
            browser.quit()


entryy()
xssInj(input(colors.CBLUE + "ex:https://xss-game.appspot.com/level1/frame?query=\nPlease enter target site:"))
