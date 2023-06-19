import json
import sys

from yt_manager import *


def get_title_time(data_dict, i):
    title_film = data_dict[i]["title"]
    time_film = data_dict[i]["time"].split(":")
    time_film = int(time_film[0]) * 60 + int(time_film[1])
    return title_film, time_film


def get_rand_video_dict(numb_of_vid_to_watch_ll, data_dict):
    if len(data_dict) <= numb_of_vid_to_watch_ll:
        return data_dict
    res = {}
    data_list = [data_dict[elem] for elem in data_dict]
    while len(res) < numb_of_vid_to_watch_ll:
        idx = random.randint(0, len(data_list)-1)
        res[f"{len(res)}"] = data_list[idx]
        data_list.remove(data_list[idx])
    return res


def main(numb_of_vid_to_watch_loc, other_film_sleep_time):
    file_name = 'data.json'
    other_devops_films = "dev ops for beginners"
    channel = "Piotr Kubon Dev Ops AI"

    with open(file_name) as json_file:
        data_dict = json.load(json_file)
        if len(data_dict) == 0:
            raise Exception("-> data file contains no elems... or does not exist in this dir")

    try:
        driver = get_init_driver()
        data_dict_spec = get_rand_video_dict(numb_of_vid_to_watch_loc, data_dict)
        for i in data_dict_spec:
            sys.stdout.write(f"=============\r\n{i}\r\n")
            # ---- watch some random film ------
            other_film_sleep_time = other_film_sleep_time * random.uniform(0.9, 1.1)
            search_for_my_video_in_youtube_search(driver, other_devops_films)
            go_to_rand_film_from_search_option(driver)
            simulate_user_scroll(driver)
            time.sleep(other_film_sleep_time)

            # --- watch my film -----
            title_film, time_film = get_title_time(data_dict_spec, i)
            channel_and_film_title = channel + " " + title_film
            search_for_my_video_in_youtube_search(driver, channel_and_film_title)
            localized_my_film = go_to_film_from_search_option(driver, title_film)
            if not localized_my_film:
                go_to_film_from_profile_page(driver, title_film)

            simulate_user_scroll(driver)
            time.sleep(time_film)
            sys.stdout.write(f"{i}    {title_film}\r\n=============\r\n")
    except Exception as eee:
        sys.stdout.write(f"\r\n=============\r\n{eee}\r\n=============\r\n")
        pass

    time.sleep(1)
    sys.stdout.write("====== END =======")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        numb_of_vid_to_watch = 15
        sleep_time = 22
        # raise Exception("Passed args. Exception -> les than 2")
    else:
        numb_of_vid_to_watch = int(sys.argv[1])
        sleep_time = int(sys.argv[2])

    main(numb_of_vid_to_watch, sleep_time)
