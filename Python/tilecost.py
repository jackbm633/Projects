floor_height = float(input("Enter the floor height (in metres): "))
floor_width = float(input("Enter the floor width (in metres): "))
cost_square_metre = float(input("Enter the cost of the floor per square metres (in pounds): "))

area = floor_height * floor_width
total_cost = area * cost_square_metre

print("The total cost for a floor of {0} metres by {1} metres with a flooring cost of".format(floor_height, floor_width))
print("£{0} per square metre is £{1}.".format(round(cost_square_metre,2), round(total_cost,2)))
