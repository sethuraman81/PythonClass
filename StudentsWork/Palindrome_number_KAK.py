#"palindrome program")

def palindrome(rang):
    for num in range(10, rang):
       st = str(num)
       if str(num) == st[::-1] :
            print("palindrum ", num)
             #print(f"{num} is palindrom")


rang= int(input("Enter the range"))
palindrome(rang)
