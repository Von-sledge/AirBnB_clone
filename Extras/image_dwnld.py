#!/usr/bin/python3

import requests

url = "https://s3.amazonaws.com/intranet-projects-files/holbertonschool-higher-level_programming+/268/logo.png"

response = requests.get(url)

if response.status_code == 200:
    with open("icon.png", "wb") as f:
        f.write(response.content)
    print("Image downloaded successfully.")
else:
    print("Failed to download the image.")
