# írj egy föggvényt, ami kiírja, hogy "Hello Functions!"
# Írj egy függvényt, ami két paramétert kap, és összeadja ezeket!
# Írj gey függvényt, ami visszaadja, hogy a paraméterként átadott szöveg, hány space karaktert tartalmaz!
# Írj egy függvényt, ami paraméterként átadott lista átlagát adja vissza
# Írj egy függvényt, ami visszadja, hogy hány magánhangzó van, a paraméterként átadott szövegben!

def print_hello():
    szoveg = "Hello Functions!"
    print(szoveg)
print_hello()


def print_osszead(param1,param2):
    osszead = param1 + param2
    print(osszead)
print_osszead(10, 10)

def print_space(param3):
    szokoz = 0
    for space_szam in param3:
        if space_szam == " ":
            szokoz +=1
    print(szokoz)
    return szokoz
#print_space("Ez egy mondtad space karakterrel")



