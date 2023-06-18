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

    sys.stdout.write(f"\r\n   000    \r\n")

    with open(file_name) as json_file:
        data_dict = json.load(json_file)

    sys.stdout.write(f"\r\n   001    \r\n")
    sys.stdout.write(f"\r\n   {data_dict}    \r\n")

    try:
        sys.stdout.write(f"\r\n   002    \r\n")
        driver = get_init_driver()
        sys.stdout.write(f"\r\n   003    \r\n")
        for i in data_dict:
            title_film = ""
            sys.stdout.write(f"\r\n   1    \r\n")
            search_for_my_video_in_youtube_search(driver, other_devops_films)
            sys.stdout.write(f"\r\n   2    \r\n")
            go_to_rand_film_from_search_option(driver)
            sys.stdout.write(f"\r\n   3    \r\n")
            other_film_sleep_time = other_film_sleep_time * random.uniform(0.9, 1.1)
            sys.stdout.write(f"\r\n   4    \r\n")
            time.sleep(other_film_sleep_time)

            sys.stdout.write(f"\r\n   other_film_sleep_time: {other_film_sleep_time}\r\n")
            sys.stdout.write(f"\r\n   hard_will___confidence_to_watch: {hard_will___confidence_to_watch}\n")

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
        sys.stdout.write(f"\r\n=============\r\n{eee}\r\n=============\r\n")
        pass

    time.sleep(1)
    print("====== END =======")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise Exception("Passed args. Exception -> les than 2")

    confidence = int(sys.argv[1])
    sleep_time = int(sys.argv[2])

    main(confidence, sleep_time)
