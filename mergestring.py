#Assume input string contain only alphabet symbol and digit wap program to sort charactors of the strng first alphabet symbloe follow by digit
#input b4a1d3
#output ABD134 
s='AVC22VGDW#WWETR'
alphat=[]
digit=[]
for ch in s:
    if ch.isalpha():
        alphat.append(ch)
    else:
        digit.append(ch)
output=''.join(sorted(alphat)+sorted(digit))
print(output)