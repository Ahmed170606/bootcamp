def getGetal(prompt = 'geef eem getal '):
    while True:
        try:
            invoer = (prompt)
            getal = int(invoer)
            return getal
        except:
            print(f'"{invoer}"dat is geen getal. Probeer nog eens')
        
katten = getGetal('honden?')
print(f'je hebt ingevoerd: {katten}')