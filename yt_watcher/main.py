import json
from yt_manager import *


file_name = 'data.json'
other_devops_films = "dev ops for beginners"
channel = "Piotr Kubon Dev Ops AI"
hard_will___confidence_to_watch = 70

with open(file_name) as json_file:
    data_dict = json.load(json_file)

try:
    driver = get_init_driver()
    for i in data_dict:
        if random.randrange(0, 100) < hard_will___confidence_to_watch:
            elem = data_dict[i]
            title_film = elem["title"]
            channel_and_film_title = channel + " " + title_film
            time_film = elem["time"].split(":")
            time_film = int(time_film[0])*60 + int(time_film[1])

            search_for_my_video_in_youtube_search(driver, other_devops_films)
            go_to_rand_film_from_search_option(driver)

            search_for_my_video_in_youtube_search(driver, channel_and_film_title)
            localized_my_film = go_to_film_from_search_option(driver, title_film, time_film)
            if not localized_my_film:
                go_to_film_from_profile_page(driver, title_film, time_film)
            simulate_user_scroll(driver)
            print("=============")
            print(f"{i}    {title_film}")
            print("=============") 
except Exception as eee:
    print("======ERROR=======")
    print(eee)
    print("=============")
    pass

time.sleep(1)
print("====== END =======")
