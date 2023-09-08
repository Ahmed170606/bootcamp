TE_RADEN_WOORD = 'python'
doorgaan = 'true'
print('welkom bij mijn supergame....')

while doorgaan == True:
    geraden_woord = input ('wat is het woord')
    if geraden_woord == TE_RADEN_WOORD:
        print (f'je hebt het woord geraden, het was: {TE_RADEN_WOORD}')
        doorgaan = False
    else:
        print('het woord is helaas fout!')