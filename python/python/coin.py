coin = int(input())

#100 = 1 dollar, 25 = 1quarter 10 = dime  5= nickel, penies = 1
dollar = 0
quarter = 0
dime = 0
nickel = 0
pennies = 0
total = coin/100

if coin >= 100:
  dollar +=  int(coin/100)
  coin -= dollar*100

if coin >= 25:
  quarter += int(coin/25)
  coin -= quarter*25

if coin >= 10:
  dime += int(coin/10)
  coin -= dime*10

if coin >= 5:
  nickel += int(coin/5)
  coin -= nickel*5

if coin >=1:
  pennies += int(coin/1)
  coin -= pennies*1
  


print(str(total)+"consist of:"+"\nDollar: "+str(dollar)+"\nQuarter: "+str(quarter)+"\nDime: "+str(dime)+"\nNickel: "+str(nickel)+"\nPennies: "+str(pennies))
