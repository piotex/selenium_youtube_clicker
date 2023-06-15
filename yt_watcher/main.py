import json
import time

from yt_watcher.yt_manager import *


channel_url = 'https://www.youtube.com/@piotrkubondevopsai/videos'
file_name = 'data.json'

with open(file_name) as json_file:
    data_dict = json.load(json_file)





driver = get_init_driver()


for i in data_dict:
    elem = data_dict[i]
    title_film = elem["title"]
    time_film = elem["time"].split(":")
    time_film = int(time_film[0])*60 + int(time_film[1])

    search_for_my_video_in_youtube_search(driver, title_film)

    # find my film in proposed ---------------------------------------------------------------------------
    localized_my_film = False
    for i in range(1, 20):
        x_path_video = f"/html/body/ytd-app/div[1]/ytd-page-manager/ytd-search/div[1]/" \
                       f"ytd-two-column-search-results-renderer/div/ytd-section-list-renderer/div[2]/" \
                       f"ytd-item-section-renderer/div[3]/ytd-video-renderer[{i}]/" \
                       f"div[1]/div/div[1]/div/h3/a/yt-formatted-string"
        res_text = driver.find_element(by=By.XPATH, value=x_path_video).text
        if res_text == title_film:
            # go to my video ---------------------------------------------------------------------------
            driver.find_element(by=By.XPATH, value=x_path_video).click()
            localized_my_film = True
            time.sleep(time_film)
            break
        driver.execute_script(f"window.scrollTo(0, {i*500})")
        time.sleep(1)

    if not localized_my_film:
        driver.get(channel_url)
        time.sleep(1)
        max_column_numb = get_max_column_number(driver)
        try:
            for row in range(1, 1000):
                for column in range(1, max_column_numb + 1):
                    x_path_video = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/' \
                                   f'ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{row}]/div/ytd-rich-item-renderer[{column}]/' \
                                   f'div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string'
                    title_m = driver.find_element(by=By.XPATH, value=x_path_video).text
                    if title_m == title_film:
                        # go to my video ---------------------------------------------------------------------------
                        driver.find_element(by=By.XPATH, value=x_path_video).click()
                        localized_my_film = True
                        time.sleep(time_film)
                        break

                if localized_my_film:
                    break
                driver.execute_script(f"window.scrollTo(0, {row * 800})")
                print(row)
                time.sleep(1)

        except Exception as eee:
            pass

    simulate_user_scroll(driver)




print(driver.title)
time.sleep(15)