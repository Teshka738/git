def read_file(mode="all"):
    try:
        with open("example.txt", "r") as file:
            if mode == "all":
                text = file.read()
                print("Чтение всего файла:")
                print(text)
            elif mode == "line":
                print("Построчное чтение:")
                for line in file:
                    print(line, end="")
            elif mode == "lines":
                lines = file.readlines()
                print("Чтение строк в виде списка:")
                print(lines)
    except FileNotFoundError:
        print("Файл не найден")

read_file("all")
print("\n")
read_file("line")
print("\n")
read_file("lines")
