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


def wait(a, name):
    WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((a, name)))


# slayt test -start
wait(By.XPATH, "//*[@id='home-slider']/div[2]/button[1]")
slaytBtn = driver.find_element(
    By.XPATH, "//*[@id='home-slider']/div[2]/button[1]")
slaytBtn.click()
# slayt test - end


sleep(5000)
