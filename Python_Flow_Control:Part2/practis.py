s=input('enter the string ')
i=0
for x in s:
    print('the string in +ve {} and -ve {} index {} is'.format(i,i-len(s),x))
    i=i+1