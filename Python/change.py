total_cost = float(input("Enter the total cost of the items: "))
paid_amount = float(input("Enter the amount of money used to pay for this item: "))

change = (paid_amount - total_cost) * 100
print("Change required to give: £",change/100)
change_temp = change

denom_values = (2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1)
denom_names = ("£20", "£10", "£5", "£2", "£1", "50p", "20p", "10p", "5p", "2p", "1p")

for i in range(len(denom_names)):
    num = 0
    while change_temp >= denom_values[i]:
        num += 1
        change_temp -= denom_values[i]
    print(denom_names[i], "x", num)
        

