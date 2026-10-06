real_temp = float(input())
desired_temp = float(input())
if real_temp > desired_temp:
    print("Охлаждение")
elif real_temp < desired_temp:
    print("Нагрев")
else:
    print("Выключен")