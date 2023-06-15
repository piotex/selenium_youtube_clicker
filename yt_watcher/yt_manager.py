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


def simulate_user_scroll(driver_loc):
    driver_loc.execute_script(f"window.scrollTo(0, {random.randint(500, 1000)})")
    time.sleep(random.uniform(0.5, 2))
    driver_loc.execute_script(f"window.scrollTo(0, -{random.randint(500, 1000)})")
    time.sleep(random.uniform(0.5, 2))
    driver_loc.execute_script(f"window.scrollTo(0, {int(random.randint(500, 1000) / 2)})")
    time.sleep(random.uniform(0.5, 2))
    driver_loc.execute_script(f"window.scrollTo(0, 0)")
    return None


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
        except Exception as eee:
            pass


def get_init_driver():
    chromedriver_autoinstaller.install()
    driver = webdriver.Chrome()
    # accept cookies ---------------------------------------------------------------------------
    try:
        accept_cookies(driver)
    except Exception as eee:
        print(eee)
    # find my chanel ---------------------------------------------------------------------------
    return driver


def get_max_column_number(driver) -> int:
    max_column_numb = 999
    try:
        for column in range(1, 999):
            x_path_video = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/' \
                           f'ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[1]/div/ytd-rich-item-renderer[{column}]/' \
                           f'div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string'
            title_m = driver.find_element(by=By.XPATH, value=x_path_video).text
            max_column_numb = column
    except Exception as eee:
        print(f'max_column_numb: {max_column_numb}')
    return max_column_numb



