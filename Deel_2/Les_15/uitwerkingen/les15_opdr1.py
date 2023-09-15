def getGetal():
    getalIngevoerd = False
    while not getalIngevoerd:
        try:
            invoer = (input('geef een getal'))
            getal = int(invoer)
            getalIngevoerd = True
        except:
            print(f'"{invoer}"dat is geen getal. Probeer nog eens')
    return getal
        
ingevoerd = getGetal()
print(f'je hebt ingevoerd: {ingevoerd} ')