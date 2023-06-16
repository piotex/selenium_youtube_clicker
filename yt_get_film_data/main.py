import json

from yt_manager import *


data_file_name = "../data.json"
channel_url = 'https://www.youtube.com/@piotrkubondevopsai/videos'

chromedriver_autoinstaller.install()
driver = webdriver.Chrome()
# accept cookies ---------------------------------------------------------------------------
# try:
#     accept_cookies(driver)
# except Exception as eee:
#     print(eee)
# find my chanel ---------------------------------------------------------------------------

driver.get(channel_url)

dict_data = {}
dict_data_counter = 0


max_column_numb = get_max_column_number(driver)


try:
    for row in range(1,1000):
        for column in range(1,max_column_numb+1):
            print((row, column))
            x_path_video = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/' \
                           f'ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{row}]/div/ytd-rich-item-renderer[{column}]/' \
                           f'div/ytd-rich-grid-media/div[1]/div[2]/div[1]/h3/a/yt-formatted-string'
            title_m = driver.find_element(by=By.XPATH, value=x_path_video).text

            x_path_video = f'/html/body/ytd-app/div[1]/ytd-page-manager/ytd-browse/ytd-two-column-browse-results-renderer/div[1]/' \
                           f'ytd-rich-grid-renderer/div[6]/ytd-rich-grid-row[{row}]/div/ytd-rich-item-renderer[{column}]/div/' \
                           f'ytd-rich-grid-media/div[1]/ytd-thumbnail/a/div[1]/ytd-thumbnail-overlay-time-status-renderer/span'
            time_m = driver.find_element(by=By.XPATH, value=x_path_video).text

            dict_data[dict_data_counter] = {}
            dict_data[dict_data_counter]["title"] = title_m
            dict_data[dict_data_counter]["time"] = time_m
            dict_data[dict_data_counter]["bot_views"] = 99
            dict_data_counter += 1

        driver.execute_script(f"window.scrollTo(0, {row*800})")
        print(row)
        time.sleep(1)

except Exception as eee:
    pass

with open(data_file_name, "w") as data_file_m:
    json.dump(dict_data, data_file_m)


print(driver.title)
time.sleep(15)
