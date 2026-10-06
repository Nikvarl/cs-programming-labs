users_data = input().split()

last_name = users_data[0].capitalize()
first_name = users_data[1][0].capitalize()
middle_name = users_data[2][0].capitalize()

print(f"{last_name} {first_name}. {middle_name}.")