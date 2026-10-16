from In_class_2 import withdraw

balance = 100

try:
    amount = int(input("Please enter the ammount you would like to withdraw."))

    balance = withdraw(amount, balance)
except: 
    print("Invalid amount")