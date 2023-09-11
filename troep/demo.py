import time

print('starting countdown for satelite')

counter = 10

while counter > 0:
    time.sleep(0.1)
    print(counter)
    counter = counter - 1   

if counter == 5:
    print('hi')