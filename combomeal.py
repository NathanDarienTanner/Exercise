burger = int(input("Enter burger selling price : "))
soda = int(input("Enter soda selling price : "))
combomeal = int(input("Enter combo meal selling price : "))
fixedprice = (burger + soda) - combomeal
print(f"The fixed price is ${fixedprice},00")