# Maak de volgende code af:
# Je moet bijbetalen als je over je minuten of je GB's heen gaat en geen onbeperkt abonnement hebt.
AANTAL_GB = 20 # Aantal GB data in je bundel
AANTAL_MINUTEN = 200 # Aantal belminuten in je bundel
ONBEPERKT = False # test ook met True
aantal_minuten_gebeld = int(input("Hoeveel minuten heb je gebeld?"))
aantal_GB_internet = int(input("Hoeveel GB's heb je gebruikt?"))


if AANTAL_GB <= aantal_GB_internet and AANTAL_MINUTEN <= aantal_minuten_gebeld: 
    print("Let op: je moet bijbetalen!")
else:
    print("Niet aan de hand gebruik je mobiel lekker verder!")