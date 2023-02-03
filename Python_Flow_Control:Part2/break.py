cart=[10,20,30,600,70,80]
for item in cart:
    if item>500:
        print('cant order this item insurance must be required')
        break
    print('processed the item',item)