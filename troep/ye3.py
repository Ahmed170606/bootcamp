import random


termen = ('string' , 'float', 'integer' , 'boolean')

term = input('geef me een type value')

if term in termen:
    print('bingo!')
else:
    print('sorry fout! Nog eens proberen')
    for pipo in termen:
        print(pipo)

X = random.randint(0,3)

print(f' de term {termen[X]} wordt vaak vergeten')