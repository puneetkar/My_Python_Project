from sys import argv
print('the lengh of commamd link argument',len(argv))
print('the list of command line argument',argv)
print('the print command line argument one by one')
for x in argv:
    print(x)