import requests

URL = "https://www.riotgames.com/en/work-with-us/jobs"
page = requests.get(URL)

print(page.text)