num = int(input())


if num > 1:
    for i in range(2, int (num/2)+1):
        if (num % i) == 0:
            print("Not Prime")
            break
        else:
            print("Prime")
            break

else:
    print("Not prime")
