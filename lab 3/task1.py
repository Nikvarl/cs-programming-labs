users_data = input()

category = users_data[:3]
year = users_data[4:8]
code = users_data[9:]
print("Категория:", category)
print("Год:", year)
print("Код:", code)
print("обратный код:", code[::-1])
