mass = input()
s = 0
first = []
splited = mass.split()
for i in splited:
    if i in first:
        print("kek")
    else:
        first.append(i)
print(first)
