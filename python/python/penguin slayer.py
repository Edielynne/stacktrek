import math

archer_x = int(input())
archer_y = int(input())
penguin_x = int(input())
penguin_y = int(input())

d = math.sqrt((penguin_x - archer_x)**2+(penguin_y - archer_x)**2)


print(f"{d :.2f}")
