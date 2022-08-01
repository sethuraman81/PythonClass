#Ask the user to enter a number. Print out the square of the number, but use the sep optional
#argument to print it out in a full sentence that ends in a period. Sample output is shown
#below.
#Enter a number: 5
#The square of 5 is 25.

_given_number = int(input("Enter a number: "))
_Square = _given_number * _given_number
print("Given number is {0}, and \n the Square of this number is {1} " .format(_given_number, _Square))