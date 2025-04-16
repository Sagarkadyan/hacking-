prices = input().split(",")
for i in range(len(prices)):
    prices[i] = int(prices[i])
items = input().split(",")
budget_per_item = int(input())

affordable_items = []
cant_afford = 0
total_needed = 0


# Write your code below
for i in range(len(prices)):
        if prices[i] > 12 :
                cant_afford+=1
        else:
                affordable_items.append(items[i])
                total_needed+=prices[i]





print("Can buy:", affordable_items)
print("Total budget needed:", total_needed)
print("Can't afford:", cant_afford)