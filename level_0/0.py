#!/usr/bin/python3
import requests

header = {
    "Content-Type": "application/x-www-form-urlencoded"
}

url = "http://158.69.76.135/level0.php"


data_post = {
    "id": "1595",
    "holdthedoor": "Submit+Query",
}

for i in range(1024):
    requests.post(url, data=data_post, headers=header)
    print("Vote: {:d} for {:s}".format(i + 1, data_post["id"]))
print("end of voting....")
