import requests
from pprint import pprint
from sys import argv


base = "http://localhost:8080"
url = "/contatos"

x = requests.get(base + url)
try: 
    pprint (x.json())
except Exception as e:
    print("erro", e)
    pprint(x.text)


# import ipdb; ipdb.set_trace()