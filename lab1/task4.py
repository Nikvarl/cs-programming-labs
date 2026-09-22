user_time = int(input())

h = user_time // 3600
m = user_time % 3600 // 60
s = user_time % 60
print(f"{h:02}:{m:02}:{s:02}")