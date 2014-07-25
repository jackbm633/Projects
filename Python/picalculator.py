import math

decimal_places = int(input("Enter the amount of decimal places you would like pi to be generated to: "))

if decimal_places > 15:
    print("Too many decimal places. Exiting.")
    exit()

pi = (math.atan(1/5) * 16) - (math.atan(1/239) * 4)

print("Pi to {0} decimal places: {1}".format(decimal_places, round(pi, decimal_places)))
