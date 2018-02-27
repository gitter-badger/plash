#!/usr/bin/env python3

from urllib.request import urlopen
import json

resp = urlopen("https://api.github.com/repos/ihucos/plash/contents/bin")
data = json.loads(resp.read().decode())
print(data)
