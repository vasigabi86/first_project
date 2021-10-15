from requests import get

response = get("https://www.training360.com/")
print(response.text)

