from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


# def test_submit1():
chrome_option = webdriver.ChromeOptions()
chrome_option.add_experimental_option('detach', value=True)

chrome_browser = webdriver.Chrome(options=chrome_option)

chrome_browser.maximize_window()
chrome_browser.get('http://127.0.0.1:5000/')

fullnametxt = chrome_browser.find_element(By.ID,"fullname")
fullnametxt.send_keys("Karen Anne")

addresstxt = chrome_browser.find_element(By.ID,"address")
addresstxt.send_keys("Paramount Ln")

phonetxt = chrome_browser.find_element(By.ID,"phone")
phonetxt.send_keys("1800 7777777")

submitbtn = show_message_button= chrome_browser.find_element(By.ID,"submit")
submitbtn.click()

#assert the Successfully entered message

output_message = chrome_browser.find_element(By.ID,'successmsg')
assert 'Form submitted successfully!' in output_message.text


