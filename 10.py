import requests
# response = requests.get("https://httpbin.org/get")
# print(response.text)
# print(f"datatype - {type(response.text)}")
response = requests.post("https://httpbin.org/post", data="Test data", headers={"h1":"Test title"})
print(response.text)