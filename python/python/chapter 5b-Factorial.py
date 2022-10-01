num = int(input())
factorial = 1 

if int(num) >= 1:
    for i in range(1,int(num)+1):
        factorial = factorial * i

    print(factorial)