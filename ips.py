from json import load

file = open("MOCK_DATA.json", encoding="utf-8")
content = load(file)
for row in content:
    print(row["ip_address"])
