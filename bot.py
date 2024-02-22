from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver import Firefox

import pyperclip
import pyautogui
import json
import time


firefox_options_1 = FirefoxOptions()
driver1 = webdriver.Firefox(options=firefox_options_1)

firefox_options_2 = FirefoxOptions()
driver2 = webdriver.Firefox(options=firefox_options_2)


driver1.get("https://chat.openai.com/")
with open("gptcookies.json", "r") as f:
    data = json.load(f)
for cookie in data:
    driver1.add_cookie(cookie)
driver1.get("https://chat.openai.com/")
driver2.get("https://www.codingame.com/home")

with open("codinggamecookies.json", "r") as f:
    data = json.load(f)
for cookie in data:
    driver2.add_cookie(cookie)

while (True):
    time.sleep(5)
    driver2.get("https://www.codingame.com/multiplayer/clashofcode")
    time.sleep(5)
    solve_button = driver2.find_element(By.CLASS_NAME, "solve-button")
    solve_button.click()
    wait = WebDriverWait(driver2, 200)
    got_it_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "got-it-button")))
    got_it_button.click()
    wait = WebDriverWait(driver2, 10)
    wait = WebDriverWait(driver2, 10)
    element = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '.cg-ide-statement, [ng-if="!apis.statement && apis.testcases"]')))
    goal = element.text
    elements_text = driver2.find_elements(By.CSS_SELECTOR, '.view-lines.monaco-mouse-cursor-text')
    template = '\n'.join([element.text for element in elements_text])
    sentence = "résous le problème suivant en python : " + goal
    input_elem = driver1.find_element(By.XPATH, '//*[@id="prompt-textarea"]')
    input_elem.send_keys(sentence)
    send_button = driver1.find_element(By.XPATH, "//*[@data-testid='send-button']")
    send_button.click()
    time.sleep(20)
    message_element = driver1.find_elements(By.XPATH, "//*[@data-message-id]//*[contains(@class, 'language-python')]")[-1]
    pyperclip.copy(message_element.text)
    time.sleep(1)
    x_coordinate = 1000
    y_coordinate = 500
    pyautogui.click(x=x_coordinate, y=y_coordinate)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.press('enter')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    wait = WebDriverWait(driver2, 1)
    submit_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "submit")))
    submit_button.click()
    time.sleep(1)
    wait = WebDriverWait(driver2, 3)
    submit_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-button")))
    submit_button.click()
    time.sleep(1)
    try:
        wait = WebDriverWait(driver2, 3)
        submit_button = wait.until(EC.presence_of_element_located((By.CLASS_NAME, "confirm-button")))
        submit_button.click()
    except:
        continue
