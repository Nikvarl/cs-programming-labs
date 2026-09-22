distance = float(input())
consumption = float(input())
price = float(input())

fuel_needed = (distance / 100) * consumption
total_cost = fuel_needed * price

print(f"Топливо: {fuel_needed:.2f} л")
print(f"Стоимость: {total_cost:.2f} руб")