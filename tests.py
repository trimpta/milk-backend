import requests

BASE = "http://localhost:5000/"

respones = requests.get( BASE + "HALLOOOOO").json()

print(respones)