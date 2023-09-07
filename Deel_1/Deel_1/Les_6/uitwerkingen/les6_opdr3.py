Leeftijd = int (input('wat is je leeftijd'))


if Leeftijd >= 16:
    print('Gefeliciteerd, je mag je brommerrijbewijs halen.')
else:
    if Leeftijd >= 12:
        answer = input('je mag rijden')
        is_member = answer == 'ja'
        if is_member:
            print('welkom terug!')