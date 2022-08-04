a = 42
i = 5
mask = 1 << i-1
if a&mask == 0:
    print("Unset")
else:
    print("Set")