
# leeftijd = int (input('sollicitatie gesprek, voer je leeftijd in: '))
# snor = 'j'  
# diploma = 'n'

# if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
#     print('Je bent aangenomen') 
# else:
#     print(input ('sorry we nemen u niet aan, tenzij u een diploma heeft: (ja/nee)'))


leeftijd = int (input('sollicitatie gesprek, voer je leeftijd in: '))
snor = 'j'  # 'j' voor ja, 'n' voor nee
diploma = 'j'  # 'j' voor ja, 'n' voor nee

if (leeftijd >= 18 and snor == 'j') or (leeftijd < 18 and diploma == 'j'):
    print("Je bent aangenomen!")
else:
    print("Je bent niet aangenomen.")