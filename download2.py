from requests import get

response = get("https://index.hu/")
szoveg = response.text
#print(response.text)
count.szoveg("koronavírus")