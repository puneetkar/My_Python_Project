s='ABCABCABCABC'
subs='ABC'
i=s.find(subs)
if i==-1:
    print('Specified substring not found')
while i!= -1:
    print('{} present at index:{}'.format(subs,i))
    i=s.find(subs,i+len(subs),len(s))
