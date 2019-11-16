age = int(input('Enter your age: '))

lon = []

if age % 2 == 1:
    for i in range(1, age+1):
        if i % 2 == 1:
            lon.append(i)
elif age % 2 == 0:
    for i in range(1, age+1):
        if i % 2 == 0:
            lon.append(i)
print(lon)