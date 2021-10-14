szoveg = "nem tudom hogy hany e betu van ebben!"
szoveg_hossza = len(szoveg)
fugveny_eleje = 0
adott_karakter = 0
e_betu = 0

while fugveny_eleje<szoveg_hossza:
    if szoveg[adott_karakter] == 'e':
        e_betu = e_betu+1
       # else e_betu = e_betu
    fugveny_eleje = fugveny_eleje+1
    adott_karakter = adott_karakter+1

print "A szöveg: " , szoveg
print "\n E betuk szama a mondatban: " , e_betu




#egyszerűbb
szoveg = "nem tudom hogy hany e betu van ebben!"
print "A szöveg: " , szoveg
print "\n 'e' betuk szama a mondatban: " , szoveg.count('e')

