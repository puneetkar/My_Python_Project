from sys import argv
print('The Number of command line Arguments:',len(argv))
print('The List of command line arguments:',argv)
print('command line argument one by one:')
for x in argv:
    print(x)