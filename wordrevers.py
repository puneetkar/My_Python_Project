s='python learning is very easy '
l=s.split()
a=l[::-1]
output=' '.join(a)
print(output)

#wap to REVERSE internal content of each word
s='python program is very easy to learn'
l=s.split()
l1=[]
for word in l:
    l1.append(word[::-1])
    output=' '.join(l1)
print(output)
#wap
s='bangalore is very beautifull city'
l=s.split(s)
l1=[]
for word in l:
    l1.append(word[::-1])
    output=''.join(l1)
print(output)