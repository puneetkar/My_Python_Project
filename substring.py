s='ABCABCABCABC'
subs=input('Enter the substring ')
i=s.find(subs)
if i==-1:
   print('Specifed string not found')
c=0
while i!=-1:
    c=c+1
    print('{} present in the index{} '.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
    print('number of occurance',c)