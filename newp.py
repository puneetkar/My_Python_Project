a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))
small=a if a<b and a<c else b if b<c else c
print("small number",small)
