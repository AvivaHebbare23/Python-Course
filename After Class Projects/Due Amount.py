total_bill = 450
print("Your total bill is $450. Please pay.\n")
amount_payed = 0

while amount_payed < total_bill:
    payment = int(input("Enter an amount to pay: "))
    amount_payed += payment
    due = total_bill - amount_payed

    if amount_payed >= total_bill:
        print("Your due is payed.")
        break
    else:
        print("Your due is: ", due)
