principal_amount = float(input("Enter the principal amount: £"))
interest_rate = float(input("Enter the interest rate (%): ")) / 100
number_of_payments = float(input("Enter the number of payments: "))

monthly_payment = principal_amount*((interest_rate*(1+interest_rate)**number_of_payments)/(((1+interest_rate)**number_of_payments)-1))

print("Your monthly payment is £{0}".format(monthly_payment))
