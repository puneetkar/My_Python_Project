s='durga prasad software solution' #split example
l=s.split()
print(l)
for x in l:
    print(x) 

l=['durga','software','solution'] #join example
s=''.join(l)    
print(s)

l=['01','04','2019']  #join example
s='+'.join(l)
print(s)

#Learning python 
s='learning python very easy' #
print(s.upper())              #LEARNING PYTHON VERY EASY
print(s.lower())              #learning python very easy
print(s.swapcase())           #
print(s.capitalize())         # learning python very easy

#WAP a programe to check whether the given 2 string are equal or not 
#by ignor case
s1=input('Enter the string ')
s2=input('enter the second string ')
if s1.lower()==s2.lower():
    print('Given string is same')
else:
    print('The Given string is not equal')

    #WAP a programe to check whether the given 2 string are equal or not 
#by ignor case
s1=input('Enter the string ').lower()
s2=input('enter the second string ').lower()
if s1==s2:
    print('Given string is same')
else:
    print('The Given string is not equal')

#WAP a program to check whether provided username and password are valid or not
# username is not case sensitive ,but password should case sensitive
username=input('Enter the username ')
passwd=input('Enter Password:')   
if username.lower()=='durga' and passwd=='anushka' :
    print('valid user')
else:
    print('Invalid user')

#WPA to convert first ans last characters as upper case and all remaining charactors should be lowser case
#given string
