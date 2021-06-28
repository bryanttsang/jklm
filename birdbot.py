# modified specifically to work against BirdBot, a ridiculously fast bot

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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

# vs bot
while 1:
    # selfturn
    while oturn.is_displayed() == False and sturn.is_displayed() == True:
        substr = driver.find_element_by_class_name("syllable").text.lower()
        s = [word for word in d if substr in word] # list of words containing substr
        s.sort(key = lambda word: sum(1 for x in l if x in word), reverse = True) # sort by occurance of unused letters
        # pick a word and remove it from the lists
        try:
            word = s[0]
            s.remove(word)
            d.remove(word)
        except:
            pass
        # input the word, update letter set
        try:
            form.send_keys(word)
            form.send_keys(Keys.ENTER)
            l = l.difference(set(word))
            if len(l) == 0:
                l = letters.copy()
        except:
            break
        time.sleep(0.25)
    time.sleep(0.25)
