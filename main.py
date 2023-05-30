import time

from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

chromedriver_autoinstaller.install()  # Check if the current version of chromedriver exists
                                      # and if it doesn't exist, download it automatically,
                                      # then add chromedriver to path

driver = webdriver.Chrome()
driver.get("https://youtube.com")
x_path = "//*[@id=\"content\"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"

driver.find_element(By.XPATH, x_path).click()

driver.get("https://youtube.com")

time.sleep(5)

text_val = "Piotr Kubon"
x_path = "//*[@id=\"search\"]"

username_input = driver.find_element(by=By.XPATH, value='//input[@id="search"]')
username_input.send_keys("john")

x_path = "//*[@id=\"search-icon-legacy\"]"

login_link = driver.find_element(by=By.XPATH, value=x_path)
login_link.click()







print(driver.title)
time.sleep(15)