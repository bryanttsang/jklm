from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import random

# destroy kids
def bot():
    while 1:
        if status == False:
            return
        if oturn.is_displayed() == False and sturn.is_displayed() == True:
            substr = driver.find_element_by_class_name("syllable").text.lower()
            s = list(filter(lambda word: substr in word, d))
            while oturn.is_displayed() == False and sturn.is_displayed() == True:
                if status == False:
                    return
                try:
                    word = random.choice(s)
                    d.remove(word)
                except:
                    pass
                try:
                    form.send_keys(word)
                    form.send_keys(Keys.ENTER)
                except:
                    break
        driver.implicitly_wait(0.25)

# load dictionary
f = open("dict.txt", "r")
d = f.read().split("\n")
f.close()

# load browser
driver = webdriver.Chrome()
driver.get("https://jklm.fun/HFSR")

# prompt for start
input("Press enter when finished loading")

# get elements
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
oturn = driver.find_element_by_class_name("otherTurn")
sturn = driver.find_element_by_class_name("selfTurn")
form = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

# start bot
status = True
t = threading.Thread(target = bot)
t.start()

# user commands
while 1:
    cmd = input("Enter command\n")
    # start
    if cmd == "s" and status == False:
        status = True
        t = threading.Thread(target = bot)
        t.start()
    # pause
    elif cmd == "p" and status == True:
        status = False
        t.join()
    # end
    elif cmd == "e":
        status = False
        t.join()
        # driver.quit() # close browser
        exit(0)
    else:
        print("Invalid command: %s\n" %cmd)
