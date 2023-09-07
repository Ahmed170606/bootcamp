cijfer = float (input ('voer het cijfer in'))

cijfer_omschrijving = {
1 : 'zeer slecht',
2 : 'slecht',
3 : "gering",
4 : "onvoldoende",
5 : "bijna voeldende",
6 : "voldoende",
7 : "ruim voldoende",
8 : "goed",
9 : "zeer goed",
10: "uitmunted"
}

if cijfer in cijfer_omschrijving:
    omschrijving = cijfer_omschrijving[cijfer]
    print(f'De omschrijving van het cijfer {cijfer} is: {omschrijving}')
    if cijfer < 6: 
        print(f'Jammer, {omschrijving} je resultaat is een {cijfer}')
    if cijfer == 6:
        print(f'Gefeliciteerd, {omschrijving} je resultaat is een {cijfer}')

else:
    print('Dit kan ik niet omzetten!')