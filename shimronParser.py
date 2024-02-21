import requests
from os import environ

sauce_username = environ["SAUCE_USERNAME"]
sauce_accesskey = environ["SAUCE_ACCESS_KEY"]

username = "oauth-shimron.trammell-9b60b"
url = "https://api.us-west-1.saucelabs.com/rest/v1/" + username + "/jobs"

jobs = requests.get(url,auth=(sauce_username,sauce_accesskey)).json()
methods = {}

for job in jobs:
    print(job["id"])
    logs = requests.get(url+"/"+job["id"]+"/assets/log.json",auth=(sauce_username,sauce_accesskey)).json()
    filterLogs = (log for log in logs if "message" not in log)
    for log in filterLogs:
        if log["method"] in methods:
            methods[log["method"]] = methods[log["method"]]+1
        else:
            methods[log["method"]] = 1

print(methods)
d
