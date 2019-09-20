from urllib.request import Request, urlopen
import json

class Slack():

    def __init__(self, *, url):
        self.url = url
        self.headers = {"Content-type": "application/json"}
        self.method = "POST"

    def post(self, **kwargs):
        data = json.dumps(kwargs).encode()
        req = Request(self.url, data=data, headers=self.headers, method=self.method)
        return urlopen(req).read().decode()
