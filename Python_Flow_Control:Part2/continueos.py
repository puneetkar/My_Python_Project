cart=[10,20,30,40,600,700,60,200,2000]
for item in cart:
    if item>500:
        print('insurance must be reqiured,just skipping')
        continue
    print('process item:',item)