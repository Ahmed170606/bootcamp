from time import sleep

aantal_meldingen = 5

oppervlakte = int(input('Hoeveel m2 vloerbedekking heeft u nodig?'))
prijs_m2 = 40

while aantal_meldingen > 0:
    print("Een moment geduld a.u.b., de scherpste prijs wordt berekend.")
    sleep(1)
    aantal_meldingen = 1

totaal = prijs_m2 * oppervlakte

print(f'Het scherpste prijs voor een oppervlakte van {oppervlakte} m2 is: Eur ' + str(totaal))


