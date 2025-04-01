def total_calculation(amount, tip):
    total = amount*(1+ 0.01*tip)
    total = round(total, 2)
    print("Please pay: ", total)

total_calculation(150, 20)