#A lot of cell phones have tip calculators. Write one. Ask the user for the price of the meal and
#the percent tip they want to leave. Then print both the tip amount and the total bill with the
#tip included.

bill_amt = float(input("Enter the bill amount: "))
tips_amt = float(input("Enter the tips amount: "))
tot_amt = bill_amt + tips_amt
print("Bill amount = {0} \nTips amount =  {1} \n ------------------- \n total bill amount = {2} \n ------------------- \n" .format(bill_amt,tips_amt,tot_amt))