s='asddf33dfef554df90'
alpha=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alpha.append(ch)
    else:
        digit.append(ch)
output=''.join(sorted(alpha)+sorted(digit))
print(output)
