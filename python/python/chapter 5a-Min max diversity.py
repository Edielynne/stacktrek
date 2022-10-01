array = []
highest = 0
lowest = 0
divisible = 0

for i in range(10):
    element = int(input())
    array.append(element)


for a in array:
    if a > highest:
        highest = a
        if lowest == 0:
            lowest = a  
    else:
        if a < lowest:
            lowest = a 

    if a %3 == 0:
        divisible += 1

print(f"Highest: {highest}\nLowest: {lowest}\n{divisible} numbers divisible by 3")






    
