#Given _a Temperature number in Celsius convert the value to Fahrenheit and print Both Celsius and Fahrenhiet values
#Formula is : (1°C × 9/5) + 32 = 33.8°F
#C- is celsius
#F - is fahrenheit

Celcs = int(input("Enter the value for Celcious: "))
Faht = (Celcs * (9/5) + 32)
print("Celcious Value given is {0}" .format(Celcs) + " \n Fahranheat value is {0}" .format(Faht))
