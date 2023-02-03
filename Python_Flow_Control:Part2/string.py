s=input('Enter the Charactor ')
if s.isalnum():
    print('Its alphanumeric charactor ')
    if s.isalpha():
        print('its alphabetic charactor')
        if s.lower():
            print('its lower chatactor')
        else:
            print('its upper digit chatactor')
    else:
        print('it is a digit') 
elif s.isspace():
    print('It is a space')
else:
    print('Its is a non space charactor')                      