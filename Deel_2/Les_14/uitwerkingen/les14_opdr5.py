namenlijst = ["thomas", "tom", "tim", "David", "gees"]


ingevoerde_naam = input("Voer een naam in: ")

try:
    namenlijst.remove(ingevoerde_naam)
    print(f"{ingevoerde_naam} is verwijderd uit de lijst.")
except ValueError:
    namenlijst.append(ingevoerde_naam)
    print(f"{ingevoerde_naam} is toegevoegd aan de lijst.")


print("Bijgewerkte lijst van namen:")
for naam in namenlijst:
    print(naam)




# Schrijf een programma dat een lijst van 5 namen maakt en vervolgens de gebruiker vraagt om een naam in te voeren. 
# Gebruik de remove functie om de opgegeven naam uit de lijst te verwijderen als deze voorkomt en print vervolgens 
# de bijgewerkte lijst.  Als de opgegeven naam niet in de lijst voorkomt, 
# gebruik dan de append functie om deze aan de lijst toe te voegen en print vervolgens de bijgewerkte lijst.