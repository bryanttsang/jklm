from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random

f = open("dict.txt", "r")
d = f.read().split("\n")
f.close()

driver = webdriver.Chrome()
driver.get("https://jklm.fun/PKEM")

input("Press enter when finished loading")

driver.switch_to.frame(driver.find_element_by_tag_name("iframe"))
oturn = driver.find_element_by_class_name("otherTurn")
sturn = driver.find_element_by_class_name("selfTurn")
form = driver.find_element_by_xpath("/html/body/div[2]/div[3]/div[2]/div[2]/form/input")

while (1):
    while oturn.is_displayed() == False and sturn.is_displayed() == True:
        substr = driver.find_element_by_class_name("syllable").text.lower()
        s = list(filter(lambda word: substr in word, d))
        word = random.choice(s)
        try:
            form.send_keys(word)
            form.send_keys(Keys.ENTER)
        except:
            break
    driver.implicitly_wait(0.1)
