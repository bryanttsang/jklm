from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import threading
import random
import time

# load dictionary
f = open("dict.txt", "r")
d = f.read().split("\n")
f.close()

# load list of letters
letters = []
for x in range(ord('a'), ord('w')):
    letters.append(chr(x))
letters.remove('k')
letters = set(letters)
l = letters.copy()

# load browser
driver = webdriver.Chrome()
driver.get("https://jklm.fun")

# prompt for start
input("Press enter when finished loading")

# get elements
driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
oturn = driver.find_element_by_class_name("otherTurn")
sturn = driver.find_element_by_class_name("selfTurn")
form = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

# destroy kids
def bot():
    while 1:
        # react to pause or end
        if status == False:
            return
        # selfturn
        if oturn.is_displayed() == False and sturn.is_displayed() == True:
            global l
            substr = driver.find_element_by_class_name("syllable").text.lower()
            s = [word for word in d if substr in word] # list of words containing substr
            s.sort(key = lambda word: sum(1 for x in l if x in word), reverse = True) # sort by occurance of unused letters
            # keep trying until not selfturn
            while oturn.is_displayed() == False and sturn.is_displayed() == True:
                # react to pause or end
                if status == False:
                    return
                # pick a word and remove it from the lists
                try:
                    word = s[0]
                    s.remove(word)
                    d.remove(word)
                except:
                    pass
                # input the word, update letter set
                try:
                    global l
                    form.send_keys(word)
                    form.send_keys(Keys.ENTER)
                    l = l.difference(set(word))
                    if len(l) == 0:
                        l = letters.copy()
                except:
                    break
                time.sleep(0.25)
        time.sleep(0.25)

# start bot
status = True
t = threading.Thread(target = bot)
t.daemon = True
t.start()

# user commands
while 1:
    cmd = input("Enter command\n")
    # start
    if cmd == "s" and status == False:
        status = True
        t = threading.Thread(target = bot)
        t.daemon = True
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
