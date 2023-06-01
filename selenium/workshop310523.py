from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()


def wait(a, name):
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((a, name)))


# girilen url full-path url olmalı.
driver.get("https://www.etiya.com")
driver.maximize_window()

# slayt test -start
# test case: open etiya.com
# click the left arrow on the slide--> expected results: previous slide (no:5) should be open.

wait(By.XPATH, "//*[@id='home-slider']/div[2]/button[1]")
slideBtn = driver.find_element(
    By.XPATH, "//*[@id='home-slider']/div[2]/button[1]")
slideBtn.click()
# slayt test - end


# chatbot test -start
# open etiya.com
# click the menu button Expected results: Dropdown menu opens
# click the product button. Expected results: Products page opens.
# scroll down the page
# click the chatbot header Expected results: Chatbot product details page opens
wait(By.ID, "menu")
menuBtn = driver.find_element(By.ID, "menu")
menuBtn.click()

wait(By.XPATH, "//*[@id='menu-container']/ul/li[2]/a")
productBtn = driver.find_element(
    By.XPATH, "//*[@id='menu-container']/ul/li[2]/a")
productBtn.click()
chatbot = driver.find_element(By.XPATH, "//*[@id='story']/div[8]/a/div[2]")
actionChains = ActionChains(driver)
actionChains.move_to_element(chatbot)
actionChains.perform()
chatbot.click()
# chatbot test -end


# Let Us Navigate You field Europe Button Test -start
# open etiya.com
# scroll down the page
# click the Europe button. Expected results: Form screen opens.
driver.get("https://www.etiya.com")
eubutton = driver.find_element(
    By.XPATH, "//*[@id='home-leadform']/div[1]/div[1]/span[1]")
actionChains = ActionChains(driver)
actionChains.move_to_element(eubutton)
actionChains.perform()
wait(By.XPATH, "//*[@id='home-leadform']/div[1]/div[1]/span[1]")
eubutton.click()
# Let Us Navigate You field Europe Button Test -end

# form test -start
wait(By.ID, "lead-send")
sendBtn = driver.find_element(By.ID, "lead-send")
action = ActionChains(driver)
action.move_to_element(sendBtn)
action.perform()

nameInput = driver.find_element(By.ID, "lead-name")
nameInput.send_keys("Aleyna Kaya")

emailInput = driver.find_element(By.ID, "lead-email")
emailInput.send_keys("aleyna@etiya.com")

titleInput = driver.find_element(By.ID, "lead-title")
titleInput.send_keys("Etiya")

messageInput = driver.find_element(By.ID, "lead-message")
messageInput.send_keys("Merhaba!!")

sendBtn.click()

# HALİT HOCAM FROM DOLUYOR AMA CLİCK YAPAMIYORUZ YARDIM EDİİİİN!!! :D

# form test -end


sleep(5000)
