###Program 1
cel = int(input("Enter the temperature in celsius:"))
fah = (cel * (9/5)) + 32
print("the temperature values in celsius and fahrenheit are",cel,"and",fah)

###Program 2
num = int(input("Enter a number:"))
num1 = num * num
print("the square value of ",num ," is ",num1,".")

###Program 3
num2 = int(input("Enter a number:"))
x = num2
print(x, 2*x , 3*x , 4*x , 5*x ,sep="---")

###Program 4
billamt = float(input("Enter the Bill Amount:"))
tip = int(input("Enter the Tip Percentage:"))
tip = billamt * (tip/100)
total =  billamt + tip
print("the Bill Amount is:",billamt,"\n the Tip:",tip,"\n Total Bill Amount is:",total)

