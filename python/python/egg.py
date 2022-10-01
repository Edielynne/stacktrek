each = 7 
dozen = 70 
quantity = int(input())
value = 0 
qcheck = quantity/12

if qcheck > 0:
    value += int(qcheck)*dozen
    quantity -= int(qcheck)*12
    value += quantity*each 
   
else:
    value += quantity*each

    
print(value)