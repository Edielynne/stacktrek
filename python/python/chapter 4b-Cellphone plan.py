call = int(input())
text = int(input())
plan= 799
plan_call= 60
plan_text = 100
add_call = 6.50
add_text = 1
prrd_fee = 25

extra_call = 0
extra_text = 0
totalbill = 0

if call > plan_call:
    extra_call = (call - plan_call)*add_call

if text > plan_text:
    extra_text = (text - plan_text)*add_text

five_percent = (plan + extra_call + extra_text + prrd_fee)*0.05
totalbill = plan + extra_call + extra_text + prrd_fee + five_percent

print(f"Call minutes: {call:.1f}\nText messages: {text:.1f}\nExcess minute charges:{extra_call:.2f}\nExcess SMS charges: {extra_text:.2f}\n911 fee: {prrd_fee:.2f}\nTax: {five_percent:.2f}\nTotal bill: {totalbill:.2f}")

