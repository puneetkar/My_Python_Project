s='asskd3433sjdh5657'
alphabet=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alphabet.append(ch)
    else:
        digit.append(ch)
output=''.join(sorted(alphabet)+(sorted(digit)))
print(output)