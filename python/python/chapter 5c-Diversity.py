import math
count = int(input())
array_gender = []

male= 0
female = 0
for i in range(count):
  gender = input()
  array_gender.append(gender)

for x in array_gender:
  if x =="m":
    male +=1
  elif x == "f":
    female +=1
    

if(female == 0):
  print(f"Males: {male}\nFemales: {female}\nAll males")
elif(male == 0):
  print(f"Males: {male}\nFemales: {female}\nAll females")
else:
  print(f"Males: {male}\nFemales: {female}")
  print(str(int(round(male / (math.gcd(male, female)),0))) + ':'+ str(int(round(female / (math.gcd(male, female)),0))))