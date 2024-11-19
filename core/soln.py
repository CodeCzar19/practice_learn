# a = int(input("enter a number :"))
# b = int(input("enter a second number :"))

# print(f"The answer is {a%b}. ") # "**" this is for power

# for increment
# x = 23
# x = x + 6
# print(x)
# price of house is 1M if buyers has good credit,they need to put down 10% otherwise they need to put 20% print the down payment.
house_price = 1000000
has_good_credit = str(input("Enter 'T' for True and 'F' for false: ")).upper()

if has_good_credit == "T":
    down_payment = 0.1 * house_price
    print(f"The down payment is ${down_payment}. Which is 10%.")
elif has_good_credit == "F":
    down_payment = 0.2 * house_price
    print(f"The down payment of the house is ${down_payment}. Which is 20%.")
else:
    print("Input Must Be T or F.")
