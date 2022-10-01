from math import floor
def numberOfDays(x):
      return 28 + (x + floor(x/8)) % 2 + 2 % x + 2 * floor(1/x)

input_days = int(input())
days = numberOfDays(input_days)
if days == 28:
  print(f"{days} or {days + 1} days")
else:
  print(f"{days} days")