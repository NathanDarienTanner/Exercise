totalbill = int(input("Enter amount of bill = "))
percentagetip = int(input("Amount of tips (%) = "))
nmbrppl = int(input("Enter number of people = "))
paymentperperson = totalbill/nmbrppl
tipowed = totalbill*(10/100)
totalperperson = paymentperperson+tipowed
print(f"Each person owes: ${paymentperperson}")
print(f"Tip per each person: ${tipowed}")
print(f"Total amount owed: ${totalperperson}")