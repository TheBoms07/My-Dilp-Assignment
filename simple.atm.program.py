# check balance
balance = 5000
pin = int(input("enter atm pin:" ))
print("Your available balance is:₦",balance)


# withdraw balance
balance = 5000
amount = int(input("Enter desired amount to withdraw:₦" ))
if amount <= balance:
    print("Withdrawal successful!" )
    balance = balance - amount
    print("Your account balance is:₦",balance)
elif amount >= balance:
    print("insufficient balance😂")


# deposit balance
balance = 5000
amount = float(input("Enter amount to be deposited:₦" ))
balance += amount
print("Deposit successful!")
print("Your new balance is:₦",balance)