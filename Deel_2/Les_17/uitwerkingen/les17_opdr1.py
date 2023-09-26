import random

aantal_gespeelde_rondes = 0
aantal_fouten = 0

while True:
    aantal_gespeelde_rondes += 1
    random_getal = random.randint(1, 5)
    
    print(f"Ronde {aantal_gespeelde_rondes}")
    
    while True:
        gebruikers_getal = int(input("Raad het getal tussen 1 en 5: "))

        if gebruikers_getal == random_getal:
            print("\033[92mJe hebt het getal goed geraden!\033[0m")
            break
        else:
            aantal_fouten += 1
            print("\033[91mJe hebt het getal niet goed geraden. Probeer opnieuw!\033[0m")
    
    print(f"Het juiste getal was {random_getal}.\n")
    
    opnieuw_spelen = input("Wil je nog een ronde spelen? (ja/nee): ")
    if opnieuw_spelen.lower() != "ja":
        break

print(f"Het spel is afgelopen. Je hebt {aantal_gespeelde_rondes} rondes gespeeld en {aantal_fouten} keer fout geraden. Bedankt voor het spelen!")


