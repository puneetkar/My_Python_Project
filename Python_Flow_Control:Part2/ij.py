n=input('enter the number')
if n<=1:
    print('its not a prime number')
else:
    is_prime=True
    for i in range(2,n):
        if n%2==0:
            is_prime=False
            break
    if is_prime==True:
            print('THis is prime number')
    else:
            print('its is not primw number')   