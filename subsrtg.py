s='ABCABCABCABCABC'
subs='ABC'
i=s.find(subs)
if i==-1:
    print('specified substring not found')
while i!=-1:
    print('{} The string in index{}'.format(subs,i))  
    i=s.find(subs,i+len(subs),len(s))