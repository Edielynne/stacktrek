starting = int(input())
ending_base = int(input())
ending_power = int(input())
value = []
final = []

for i in range (starting,ending_base + 1):
    for j in range(2,ending_power+1):
        value.append(str(i**j))
    final.append(",".join(value))
    value.clear()


print("\n".join(final))


