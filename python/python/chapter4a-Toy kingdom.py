donation = float(input("Target Donation:"))
puzzle = int(input("Number of Puzzles:"))
doll = int(input("Number of Talking Dolls:"))
bear = int(input("Number of Teddy Bears:"))
pokemon = int(input("Number of Pokemons:"))
truck = int(input("Number of Big Toy Truck:"))

puzzle_price = 14
doll_price = 3
bear_price = 20.2
pokemon_price = 8.20
truck_price = 10.65

total_order = puzzle + doll + bear + pokemon + truck 
total_price = (puzzle * puzzle_price) + (doll * doll_price) + (bear * bear_price) + (pokemon * pokemon_price) + (truck * truck_price) 

if total_order >= 50:
    total_price -= total_price * .25
    total_price -= total_price * .10

else:
    total_price -= total_price * .10


if total_price >= donation:
    remaining_money = total_price - donation

    print (f"Yes! {remaining_money:.2f} dollars left.")

elif total_price < donation:
    shortage = donation - total_price

    print (f"Not enough money!{shortage:.2f} dollars needed.")


   