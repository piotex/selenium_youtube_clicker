import random
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from yt_watcher.yt_manager import *




title_film = "DevOps Full Project - 01 - Przykład i omówienie"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
# accept cookies ---------------------------------------------------------------------------
try:
    accept_cookies(driver)
except Exception as eee:
    print(eee)
# find my chanel ---------------------------------------------------------------------------
search_for_my_video_in_youtube_search(driver, title_film)

# get proposed videos ---------------------------------------------------------------------------
for i in range(1, 10):
    x_path_video = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/div[1]/div/div[1]/div/h3/a/yt-formatted-string"
    res_text = driver.find_element(by=By.XPATH, value=x_path_video).text
    if res_text == title_film:
        # go to my video ---------------------------------------------------------------------------
        driver.find_element(by=By.XPATH, value=x_path_video).click()
        time.sleep(2)
        # x_path_show_desc = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/ytd-text-inline-expander/tp-yt-paper-button[1]"
        # driver.find_element(by=By.XPATH, value=x_path_show_desc).click()
        time.sleep(2)
        for j in range(1,15):
            # click ceneo link ---------------------------------------------------------------------------
            x_path_ceneo_link = "/html/body/ytd-app/div[1]/ytd-page-manager/ytd-watch-flexy/div[5]/div[1]/div/div[2]/ytd-watch-metadata/div/div[3]/div[1]/div/ytd-text-inline-expander/div[1]/span[1]/yt-attributed-string/span/span[2]/a"
            res_text = driver.find_element(by=By.XPATH, value=x_path_ceneo_link).text
            if "https://" in res_text:
                driver.find_element(by=By.XPATH, value=x_path_ceneo_link).click()
                time.sleep(2)
                driver.switch_to.window(driver.window_handles[1])
                # click random product in ceneo ----------------------------------------------------------------------
                k = random.randint(1, 5)
                x_path_ceneo_zobacz = f"/html/body/div[1]/div[2]/div[2]/div[2]/div/div[4]/div/div[1]/div[3]/div[2]/div/div/div[2]/div/div[1]/a[{k}]/div[2]/div[2]/span"
                driver.find_element(by=By.XPATH, value=x_path_ceneo_zobacz).click()
                driver.switch_to.window(driver.window_handles[2])
                time.sleep(2)

                # go to product page ----------------------------------------------------------------------
                simulate_user_scroll(driver)
                go_to_product_page(driver)

                driver.switch_to.window(driver.window_handles[0])
                break

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------





print(driver.title)
time.sleep(15)