def describe_person(name, age=30):
    print("Имя:", name)
    print("Возраст:", age)

print('Введите имя:')
name = input()
print('Хотите ввести возраст? y/n')
ch = input()

if ch == "y":
    print('Введите возраст:')
    age = int(input())
    describe_person(name, age)
else:
    describe_person(name)