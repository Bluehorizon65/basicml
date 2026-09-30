import requests

url="http://127.0.0.1:5000/inputs"

data={
    "name":"Hisham",
    "age":21

}

response=requests.post(url,json=data)
print(response.json())