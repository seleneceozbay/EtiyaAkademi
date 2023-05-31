# selenium.py şeklinde isimlendirme yapma.
# otomatize test edebilmek için önce manuel testler tamamlanmış olmalı.

# import selenium

from selenium import webdriver
from time import sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.Chrome()

# girilen url full-path url olmalı.
driver.get("https://www.etiya.com")
driver.maximize_window()

# defensive testing
# workshop görevi => bu kısmı fonksiyon haline getir.
WebDriverWait(driver, 5).until(
    expected_conditions.visibility_of_element_located((By.CLASS_NAME, "lang-select")))
languageSelector = driver.find_element(By.CLASS_NAME, "lang-select")
languageSelector.click()


turkishLanguage = driver.find_element(
    By.XPATH, "//*[@id='etiya']/header/div/div[2]/div[1]/div[2]/div[1]/a")
turkishLanguage.click()
searchBtn = driver.find_element(By.ID, "search-btn")
searchBtn.click()
searchInput = driver.find_element(By.ID, "search-input")
searchInput.send_keys("merhaba")
searchIcon = driver.find_element(
    By.XPATH, "//*[@id='search-box']/form/div/button")
searchIcon.click()

# ActionChains
driver.get("https://www.etiya.com")
button = driver.find_element(
    By.XPATH, "//*[@id='home-leadform']/div[1]/div[1]/span[1]")
actionChains = ActionChains(driver)
actionChains.move_to_element(button)
actionChains.click()
actionChains.perform()
##
sleep(5000)


# form test -start
# butonun olduğu kısma scroll yapılmalı.


# from test - end


# slayt button test -start
# slatt button test -end
