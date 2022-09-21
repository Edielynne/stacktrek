month = int(input())

if month == 2:
    print("28 days")
elif month <=7:
    if month % 2 == 1:
        print ("31 days")
    else:
        print("30 days")
else:
    if month %2 == 0:
        print("31 days")
    else:
        print("30 days")


