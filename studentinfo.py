n=eval(input('Enter student data:'))
d={}
for i in range(n):
    name=input('Enter the student name:')
    marks=int(input('Enter the student marks'))
    d[name]=marks

print('Student insertion completed.....')

print('*'*30)
print('NAME', '\t\t','MARKS')
print('*'*30)
for k ,v in d.items():
    print(k,'\t\t',v)
print('Search Opertion started')
while True:
    name=input('Enter the student name..')
    marks=d.get(name,-1)
    if marks==-1:
        print('student not found')
    else:
        print('Marks of',name,'are',marks)
    option=input('Do you want to find another student marks[yes|no]:')
    if option=='no':
        break
print('Thanks for using our application')