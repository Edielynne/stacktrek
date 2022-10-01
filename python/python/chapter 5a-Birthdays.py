age = int(input())
washing_machine_price = float(input())
toys = int(input())
even_age = age // 2
number_toys = age - age // 2
money = 0
money_saved = 0

for i in range(even_age):
    money = money + 10
    money_saved = money_saved + money

    print(money_saved)

sold_toys = number_toys * toys 
total_saved = money_saved + sold_toys


if washing_machine_price > total_saved:
    money_needed = washing_machine_price - total_saved

    print(f"Yes! you still have {money_saved} left")

else:
    money_needed = total_saved - washing_machine_price
    print(f"No! you still  {money_needed}")




    
        

