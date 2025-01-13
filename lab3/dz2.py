def write_to_file():
    user_input = input("Введите текст для записи в файл: ")
    with open("user_input.txt", "a") as file:
        file.write(user_input + "\n")
    print("Текст записан в файл user_input.txt.")
r5rf
write_to_file()