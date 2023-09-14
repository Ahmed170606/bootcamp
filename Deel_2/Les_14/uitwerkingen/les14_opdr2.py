getallenlijst = [1, 2, 3, 4, 5]

index = int(input("Voer een index in (0-4) om een getal te verwijderen: "))

if 0 <= index < len(getallenlijst):
    verwijderd_getal = getallenlijst.pop(index)
    print(f"het verwijderde cijfer wordt dan: {verwijderd_getal}")
    print("De bijgewerkte lijst:")
    print(getallenlijst)
else:
    print("Ongeldige index. Voer een index in tussen 0 en 4.")



#Schrijf een programma dat een lijst van 5 getallen maakt en vervolgens de gebruiker 
# vraagt om een index in te voeren.
# Gebruik de pop functie om het getal op de opgegeven index uit de lijst te verwijderen
 #print vervolgens het verwijderde getal en de bijgewerkte lijst.