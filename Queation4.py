sec = int(input("Enter seconds: "))

hours = sec // 3600
sec = sec % 3600
minutes = sec // 60
seconds = sec % 60

print(hours, "hours", minutes, "minutes", seconds, "seconds")
