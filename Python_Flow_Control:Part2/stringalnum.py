print('Durga786'.isalnum()) #true
print('Durga786'.isalpha()) #false
print('Durga'.isalpha())    #true
print('Durga786'.isdigit()) #false
print('786'.isdigit())      #true
print('abc'.islower())     #true
print('aabc123'.islower())  #
print('ABC'.isupper())
print('Durga Software Solution'.istitle())
print('Durga software solution'.istitle())
print('     '.isspace())

#wAP a program to check the type of charactor enterd from the 
#keyboard
s=input('Enter any string ')
if s.isalnum():
    print('its alphanumber charactor')
    if s.isalpha():
        print('Its alphabet charactor')
        if s.islower():
                print('Its lower charactor')
        else:
            print('it upper case')
    elif s.isspace():
        print('Its a space charactor')
    else:
        print('its non spacial charactor')                