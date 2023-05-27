vowels=['a','e','i','o','u']
word=input('Enter any string :')
result = [ch for ch in vowels if ch in word]
print(result)
print('the Number of unique vowels',len(result))