users_data = input()
users_data = (
    users_data
    .replace("+", "")
    .replace("(", "")
    .replace(")", "")
    .replace("-", "")
    .replace(" ", "")
)
print(users_data)