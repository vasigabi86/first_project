from json import load

file = open("game.json")
content = load(file)

characters = content["characters"]
for character in characters:
    print(character["characterName"])