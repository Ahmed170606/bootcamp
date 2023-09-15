fruitlijst = ["appel", "banaan", "peer", "sinaasappel", "kiwi"]

verwijderen_fruit = input("Voer een fruitsoort in om te verwijderen: ")

try:
    fruitlijst.remove(verwijderen_fruit)
    print(f"{verwijderen_fruit} is verwijderd uit de lijst.")
except ValueError:
    print(f"{verwijderen_fruit} is niet gevonden in de lijst.")

print("Bijgewerkte lijst van fruitsoorten:")
for fruit in fruitlijst:
     print(fruit)


# Schrijf een programma dat een lijst van fruitsoorten maakt en vervolgens de gebruiker vraagt om een
# fruitsoort in te voeren. Gebruik de remove functie
# om het opgegeven fruit uit de lijst te verwijderen en print vervolgens de bijgewerkte lijst.