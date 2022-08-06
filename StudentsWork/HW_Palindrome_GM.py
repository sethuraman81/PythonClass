#To find Palindrome for number from 1 to 1000

for a in range(1,1000):
    if(a>10):
        for j in range(1,3):
            b = str(a)
            lent = len(b)
            len1 = lent%2
            if len1 == 1:
                len2 = len1//2 +1
                if(b[::j]==b[::-j] and b[::len2]==b[::1]):
                    print(b)



