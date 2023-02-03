cart=[10,20,30,600,40,50]
for item in cart:
    if item>500:
        print('this item required insurance')
        break
    print('processing item:',item)
else:
    print('congrats, all item process successfully')