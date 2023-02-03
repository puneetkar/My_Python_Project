
words_upto_19=['','one','two','three','four','five','six','seven','eight','nine','ten','eleven','twelve','thirteen','fourteen','fiften','sixteen','seventeen','eighteen','nineteen']

word_for_tens=['','','twenty','thirty','forty','fifty','sixty','seventy','ninety','twenty']

n=int(input('enter the number from 0 -90 : '))
output=''
if n==0:
    output='ZERO'
elif n<=19:
    output=words_upto_19[n]  
elif n<=99:
    output=word_for_tens[n//10]+" "+words_upto_19[n%10]
else:
    output='Please enter a value from 0 to 99 only'
print(output)        