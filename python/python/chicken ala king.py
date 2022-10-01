import math

initial_velocity = int(input())
angle = int(input())
time = float(input())

gravity = 9.81
thata = angle*(math.pi/180)

x = initial_velocity* math.cos(thata)*time
y = (initial_velocity* math.sin(thata)*time) - (0.5*gravity*(time**2))

print (f"{round(x)}, {round(y)}")