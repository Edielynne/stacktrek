array_number = [10, 54, 21, 32, 11, 18, 12, 3, 5, 20]
h = 0
l = 0
div = 0

for i in array_number:
    if i > h:
        h = i
    else:
        if l == 0:
            l = i
        elif i < l:
            l = i
    
    if i % 3 ==0:
        div += 1

print(f'Highes: {h} \n Lowest {l} Divisible: {div}')
