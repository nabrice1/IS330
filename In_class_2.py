def withdraw(amount, balance):
    if amount > balance:
        print("You are poor.")

    return balance - amount 