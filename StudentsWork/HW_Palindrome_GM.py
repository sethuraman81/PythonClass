#To find Palindrome for number from 1 to 1000

for a in range(1,1000): #500
    if(a>10):
        for j in range(1,3):#2
            b = str(a) #555
            lent = len(b) #3
            len1 = lent%2 #1
            if len1 == 1:
                len2 = len1//2 +1 #1
                #555 == 555
                #55 == 55
                #555 == 555
                if(b[::j]==b[::-j] and b[::len2]==b[::1]):
                    print(b)



