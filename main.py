import random
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By

def accept_cookies(driver_loc):
    yt_url = "https://youtube.com"
    x_path = "//*[@id=\"content\"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"
    driver_loc.get(yt_url)
    driver_loc.find_element(By.XPATH, x_path).click()

def search_for_my_video_in_youtube_search(driver_loc, title_film):
    yt_url = "https://youtube.com"
    channel = "Piotr Kubon Dev Ops AI"
    text_val = channel + " " + title_film
    x_path_search_inp = '//input[@id="search"]'
    x_path_search_btn = "//*[@id=\"search-icon-legacy\"]"

    driver_loc.get(yt_url)
    time.sleep(2)
    driver_loc.find_element(by=By.XPATH, value=x_path_search_inp).send_keys(text_val)

    driver_loc.find_element(by=By.XPATH, value=x_path_search_btn).click()
    time.sleep(2)

def simulate_user_scrole(driver_loc):
    driver_loc.execute_script(f"window.scrollTo(0, {random.randint(500, 1000)})")
    time.sleep(random.uniform(0.5, 2))
    driver_loc.execute_script(f"window.scrollTo(0, -{random.randint(500, 1000)})")
    time.sleep(random.uniform(0.5, 2))
    driver_loc.execute_script(f"window.scrollTo(0, {int(random.randint(500, 1000) / 2)})")
    time.sleep(random.uniform(0.5, 2))

def go_to_product_page(driver_loc):
    x_path_prod_list = [
        "/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/section/ul/li/div/div[1]/div[2]/a",
        "/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/section/ul/li[1]/div/div[1]/div[2]/a",
        "/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/section[1]/ul/li/div/div[1]/div[2]/a",
        "/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/section[1]/ul/li[1]/div/div[1]/div[2]/a",
        "/html/body/div[1]/div[3]/div[2]/div/div/div[1]/div[5]/div[2]/section[1]/ul/li[1]/div/div[1]/div[2]/a"
    ]
    for x_path_prod in x_path_prod_list:
        try:
            driver_loc.find_element(by=By.XPATH, value=x_path_prod).click()
            break
        except Exception:
            pass

title_film = "DevOps Full Project - 01 - Przykład i omówienie"

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
# accept cookies ---------------------------------------------------------------------------
accept_cookies(driver)
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
                simulate_user_scrole(driver)
                go_to_product_page(driver)

                driver.switch_to.window(driver.window_handles[0])
                break

# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------
# ---------------------------------------------------------------------------





print(driver.title)
time.sleep(15)