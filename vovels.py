vowels=['a','e','i','o','u']
word=input('Enter the any string:')
result=[]
for ch in word:
    if ch in vowels:
            result.append(ch)
print(result)
print('The Number if unique vowels',len(result))