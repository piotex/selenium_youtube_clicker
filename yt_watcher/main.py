import json
import sys

from yt_manager import *


def get_title_time(data_dict, i):
    title_film = data_dict[i]["title"]
    time_film = data_dict[i]["time"].split(":")
    time_film = int(time_film[0]) * 60 + int(time_film[1])
    return title_film, time_film


def main(confidenceee, other_film_sleep_time):
    file_name = '../data.json'
    other_devops_films = "dev ops for beginners"
    channel = "Piotr Kubon Dev Ops AI"
    hard_will___confidence_to_watch = confidenceee

    with open(file_name) as json_file:
        data_dict = json.load(json_file)

    sys.stdout.write(f"\rother_film_sleep_time: {other_film_sleep_time}")
    sys.stdout.write(f"\rhard_will___confidence_to_watch: {hard_will___confidence_to_watch}")
    try:
        driver = get_init_driver()
        for i in data_dict:
            title_film = ""
            search_for_my_video_in_youtube_search(driver, other_devops_films)
            go_to_rand_film_from_search_option(driver)
            time.sleep(other_film_sleep_time * random.uniform(0.9, 1.1))

            if random.randrange(0, 100) < hard_will___confidence_to_watch:
                title_film, time_film = get_title_time(data_dict, i)
                channel_and_film_title = channel + " " + title_film

                search_for_my_video_in_youtube_search(driver, channel_and_film_title)
                localized_my_film = go_to_film_from_search_option(driver, title_film, time_film)
                if not localized_my_film:
                    go_to_film_from_profile_page(driver, title_film, time_film)
                time.sleep(time_film)

            simulate_user_scroll(driver)
            print(f"=============\r\n{i}    {title_film}\r\n=============")
    except Exception as eee:
        print(f"=============\r\n{eee}\r\n=============")
        pass

    time.sleep(1)
    print("====== END =======")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Passed args. Exception -> les than 2")

    confidence = int(sys.argv[1])
    sleep_time = int(sys.argv[2])

    main(confidence, sleep_time)
