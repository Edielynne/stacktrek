

total_amount = int(input())
tax = total_amount * .12

new_amount = total_amount - tax 
emergency_fund = new_amount * .10
accommodation = new_amount - emergency_fund

tax = "{:.2f}".format(tax)
emergency_fund = "{:.2f}".format(emergency_fund)
accommodation = "{:.2f}".format(accommodation)

print("Tax:", tax)
print("Emergency Fund:", emergency_fund)
print("Accommodation:", accommodation)






