human_years = int(input())

if human_years <=2:
   print(human_years * 10.5)

elif human_years > 2:
   first_two_years = 10.5 * 2
   after_two_years = human_years - 2
   total_years = first_two_years + (after_two_years * 4)

   print (int (total_years))

else:
    print ("please enter number:")
