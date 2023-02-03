l=[10,20,0,30,40,0,50]
for x in l:
    if x==0:
        print('hello stupid,how we can divide with zero')
        continue
    print('100/{} = {} '.format(x,100//x))