s=input('Enter the given string ')
i=0
print('these are even string')
while i<len(s):
    if i%2 ==0:
        print(s[i])
    i=i+2
print('odd string')
i=1
while i<len(s):
    print(s[i])
    i=i+2