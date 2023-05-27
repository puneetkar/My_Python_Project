n=int(input('enter the stuent details'))
d={}
for i in range(n):
    name=input('enter the student name')
    marks=int(input('enter the student marks'))
    d[name]=marks

    
print('*'*30)
print('NAME','\t\t','MARKS')
print('*'*30)
for name in d:
    print(name,'\t\t',d[name])


