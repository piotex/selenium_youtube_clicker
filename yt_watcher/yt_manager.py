import random
import time
from selenium import webdriver
import chromedriver_autoinstaller
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


def accept_cookies(driver_loc):
    yt_url = "https://youtube.com"
    x_path = "//*[@id=\"content\"]/div[2]/div[6]/div[1]/ytd-button-renderer[2]/yt-button-shape/button/yt-touch-feedback-shape/div/div[2]"
    driver_loc.get(yt_url)
    driver_loc.find_element(By.XPATH, x_path).click()


def search_for_my_video_in_youtube_search(driver_loc, text_val):
    yt_url = "https://youtube.com"
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

def go_to_film_from_profile_page(driver, title_film):
    channel_url = 'https://www.youtube.com/@piotrkubondevopsai/videos'
    driver.get(channel_url)
    time.sleep(1)
    max_column_numb = get_max_column_number(driver)
    for row in range(1, 1000):
        for column in range(1, max_column_numb + 1):
            x_path_video = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/' \
                           f'ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{row}]/div/ytd-rich-item-renderer[{column}]/' \
                           f'div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string'
            title_m = driver.find_element(by=By.XPATH, value=x_path_video).text
            if title_m == title_film:
                driver.find_element(by=By.XPATH, value=x_path_video).click()
                return None

def check_exists_by_xpath(driver, xpath):
    try:
        driver.find_element(by=By.XPATH, value=xpath)
    except NoSuchElementException:
        return False
    return True

def get_ytd_item_x_path_video(driver, film_numb):
    ytd_item_section_renderer = -1
    x_path_video = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/" \
                   f"ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/" \
                   f"ytd-item-section-renderer/div[3]/ytd-video-renderer[{film_numb}]/" \
                   f"div[1]/div/div[1]/div/h3/a/yt-formatted-string"
    if check_exists_by_xpath(driver, x_path_video):
        return x_path_video

    scroll = 100
    for i in range(1, 16):
        scroll += random.randrange(100, 200)
        driver.execute_script(f"window.scrollTo(0, {scroll})")
        time.sleep(1)
        x_path_video = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/" \
                       f"ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/" \
                       f"ytd-item-section-renderer[{i}]/div[3]/ytd-video-renderer[{film_numb}]/" \
                       f"div[1]/div/div[1]/div/h3/a/yt-formatted-string"
        if check_exists_by_xpath(driver, x_path_video):
            return x_path_video

    raise Exception("get_ytd_item_section_renderer -> element not found :(")



def go_to_film_from_search_option(driver, title_film):
    scroll = 0
    for i in range(1, 16):
        scroll += random.randrange(100, 200)
        x_path_video = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/" \
                       f"ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/" \
                       f"ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/" \
                       f"div[1]/div/div[1]/div/h3/a/yt-formatted-string"
        res_text = driver.find_element(by=By.XPATH, value=x_path_video).text

        if res_text == title_film:
            driver.find_element(by=By.XPATH, value=x_path_video).click()
            return True
    return False


def go_to_rand_film_from_search_option(driver):
    rand_film = random.randrange(1, 16)
    x_path_video = get_ytd_item_x_path_video(driver, rand_film)
    driver.find_element(by=By.XPATH, value=x_path_video).click()

