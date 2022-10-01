books = int(input())
shipping = books -1
discount = 24.95*.40
new_price = 24.95 - discount
total_price = new_price * books
total = total_price + shipping * .75+3

print(total)
