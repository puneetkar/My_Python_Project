from sys import argv
print('lengh of argv',len(argv))
print('list of argv',argv[1:])
print('command line argument one by one')
for x in argv:
    print(x)