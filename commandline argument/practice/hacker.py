
n= int(input('enter the number' .strip()))
if n % 2 != 0:
    print("Weird")
else:
    if n >= 2 and n <= 5:
        print('not Weird')
    elif n >= 6 and n <= 20:
        print('Weird')
    elif n > 20:
        print('Not Weird')
