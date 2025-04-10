n1 = float(input())
n2 = float(input())
n3 = int(input())
bill_amount=n1 


tip_amount = (n2 / 100) * bill_amount
total_amount = tip_amount + bill_amount
split = total_amount /n3

print("Bill Split Calculator")
print(f"Total (including tip): ${total_amount}")
print(f"Each person pays: ${split}")
