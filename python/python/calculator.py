
def add(num1, num2):
    result = num1 + num2
    return f"result = {num1} + {num2} = {result}"

def multiply(num1,num2):
    result = num1 * num2 
    return f"result = {num1} + {num2} = {result}"

def subtraction(num1, num2):
    result = num1 - num2
    return f"result = {num1} + {num2} = {result}"

def divide(num1, num2):
    result = num1 / num2
    return f"result = {num1} + {num2} = {result}"


print("Please select operator: \n"
    "1. add\n" 
    "2. multiply\n" 
    "3. subtraction\n" 
    "4. divide\n" )


select = int(input("select operator from 1.,2.,3.,4.,:"))


while select > 4:
    print("Invalid operator, Please select operator: \n"
    "1. add\n" 
    "2. multiply\n" 
    "3. subtraction\n" 
    "4. divide\n" )
    select = int(input("select operator from 1.,2.,3.,4.,:"))

number_1 = int(input("Enter first number:"))
number_2 = int(input("Enter second number:"))


if select == 1:
    print(add(number_1, number_2))

elif select == 2:
    print(multiply(number_1, number_2))

elif select == 3:
    print(subtraction(number_1, number_2))

elif select == 4:
    print(divide(number_1, number_2))

else:
    print("Invalid")



