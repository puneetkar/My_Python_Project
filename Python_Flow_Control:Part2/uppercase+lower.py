#WAP starting string should be Upper case and end string is lower case
s=input('Enter the number ')
output=s[0].upper()+s[1:len(s)-1].lower()+s[-1].upper()
print(output)

#checking starting and ending part of the string
s='python is a easy '
print(s.startswith('pyth'))
print(s.startswith('pty'))
print(s.endswith('easy '))