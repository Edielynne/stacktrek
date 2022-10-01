import math

hours = 24
current_time = 14
alarm = 535

clock_hours = (alarm - current_time)/hours


print(f"{math.floor(clock_hours) :.2f}")


