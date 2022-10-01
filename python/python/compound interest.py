p = int(input("Enter the principal amount:"))
r = float(input("Enter the interest rate:"))
n = int(input("Enter number of years:"))

interest_rate = p*(1+ r/100)**n
two_decimal = "{:.2f}".format(interest_rate)

print(two_decimal)
