import json
import os
import requests

from ygolib import YGO_API_ENDPOINT


def verify_download_directory():
    if not os.path.isdir("./cards"):
        os.mkdir("./cards")
        print("Created /cards/ directory")


def get_cached_image(img_url):
    img_file = img_url.split("/")[-1]
    print(f"image {img_file}", end=" ")
    img_local = f"./cards/{img_file}"
    if not os.path.exists(img_local):
        with open(img_local, "wb") as img_writer:
            img_response = requests.get(img_url)
            img_writer.write(img_response.content)
            print("Downloaded")
    else:
        print("Already present")
    return img_local


def get_cached_data(card_id):
    print(f"Card {card_id}", end=" ")
    local_data = f"./cards/{card_id}.json"
    card_data = None
    if not os.path.exists(local_data):
        response = requests.get(YGO_API_ENDPOINT, params={"id": card_id})
        if response.status_code != 200:
            print("is invalid")
            return card_data
        with open(local_data, "w") as json_writer:
            card_data = json.loads(response.text)
            json.dump(card_data, json_writer, indent=2)
            print("Downloaded")
    else:
        print("Already present")
        with open(local_data, "r") as json_reader:
            card_data = json.load(json_reader)
    return card_data
