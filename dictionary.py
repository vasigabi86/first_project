products = {"orange": 30, "apple": 50, "bread": 10}
print(products["orange"])

products["orange"] = 29
print(products)

products["milk"] = 16
print(products)

my_products = {}
print(products)
my_products["bread"] = 88
print(my_products)

del(products["orange"])
print(products)


for (key, value) in products.items():
    print(key[0] + " " + str (value[1]))

john = {
    "name": "John",
    "age": 30,
    "addr": {
        "city": "Bud"
    }

}

print((john["addr"]["city"]))

