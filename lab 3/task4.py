users_data = input().split(";")

number = users_data[0]
where_from = users_data[1]
where = users_data[2]
time = users_data[3]
price = users_data[4]
print(f"Поезд: {number}")
print(f"Маршрут: {where_from} - {where}")
print(f"Отправление: {time}")
print(f"Цена: {float(price):.2f}ч руб")
