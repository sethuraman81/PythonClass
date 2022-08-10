num= int(input("enter a number: "))
bin= bin(num) # converting to binary
print(bin)
rev= bin[2:] #truncating first two postion as it ontain 0b
rev= rev[::-1] #reversing the value
print(rev)
#print(len(rev))
while len(rev) <= 8 :
    rev = "0" + rev  #add in zeros to get 8 digit number
print(rev)
dec=int(rev,2) # converting to Decimal number
print(dec)

