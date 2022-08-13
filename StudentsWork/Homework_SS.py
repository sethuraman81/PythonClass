"""1) Given a Temperature number in Celsius convert the value to Fahrenheit and print Both Celsius and Fahrenhiet values
Formula is : (1°C × 9/5) + 32 = 33.8°F
C- is celsius
F - is fahrenheit

2) Ask the user to enter a number. Print out the square of the number, but use the sep optional
argument to print it out in a full sentence that ends in a period. Sample output is shown
below.
Enter a number: 5
The square of 5 is 25.

3)Ask the user to enter a number x. Use the sep optional argument to print out x, 2x, 3x, 4x,
and 5x, each separated by three dashes, like below.
Enter a number: 7
7---14---21---28---35

4) A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
the percent tip they want to leave. Then print both the tip amount and the total bill with the
tip included."""

"""1"""
"""celsius = float(input("Enter the Temperature:"))
fahrenheit = (celsius * 9 / 5) + 32
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit' % (celsius, fahrenheit))



number = int(input("Enter a Number:"))
square = number ** 2
print('The square of %d is %d' % (number , square))


x = int(input("Enter a Number:"))
print(x, x*2, x*3, x*4, x*5, sep="---")





Bill = float(input("Enter the Bill Amount"))
Tip1 = int(input("Enter the Tips"))
Tip2 = (Bill * Tip1/100) + Bill
print('The %.2f is Bill Amount  %d is Tip Amount amd %d is Total Amount  ' % (Bill, Tip1, Tip2))


palindrome = int(input("Enter the Maximum Value:"))
print("palindrome numbers 1 and %d are:"% palindrome)
for num in range(1, palindrome + 1):
    temp = num
    reverse = 0
    while(temp > 0):
        reminder = temp % 10
        reverse=(reverse * 10)+reminder
        temp = temp//10
    if(num == reverse):
        print("%d"%num,end=' ')"""



"""list Method"""
"""append"""
List = ['sasi','python','class']
print(List)
List.append('work')
print(List)
"""clear"""
list=['sasi','python','class']
print(list)
list.clear()
print(list)

"""copy"""
lst=['python','list','append']
lst1=lst.copy()
lst1.append("copy")
print(lst)
print(lst1)
"""count"""
lst2=['python','list','append']

print(lst2.count("python"))
print(lst2.count(" "))



"""extend """
list = ['sasi','python']
print(list)
list.extend(['developer','datascience'])
print(list)

"""index"""
A = ['sasi','python','developer','datascience']
print(A.index('developer'))
print(A.index('developer',0))

"""insert"""

list1 = ['sasi','python']
print(list1)
list1.insert(0,'python')
print(list1)
list1.insert(3,'developer')
print(list1)


"""pop"""
list2 =  ['sasi','python','developer','datascience']
print(list2)
list2.pop()
print(list2)
list2.pop(2) #with index
print(list2)


"""remove"""
list3 =  ['sasi','python','developer','datascience']
print(list3)
list3.remove('sasi')
print(list3)

"""reverse"""
list4 = ['sasi','python','developer','datascience']
print(list3)
list4.reverse()
print(list4)

"""sort"""
list5 = [10,5,9,3,4,8,6,7,1,2]
print(list5)
list5.sort()
list5.sort(reverse=False)
print(list5)
list5.sort(reverse=True)
print(list5)












