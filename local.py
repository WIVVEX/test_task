import requests
res = requests.get("http://127.0.0.1:3213/api/cities/city")
print(res.json())