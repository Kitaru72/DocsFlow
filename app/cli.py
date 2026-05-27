def ask_positive_int(prompt):
    while True:
        user_input = input(prompt)
        user_input = user_input.strip()

        try:
            number = int(user_input)

            if number <= 0:
                print("Ошибка: введенное число должно быть больше 0")
                continue

            return number

        except ValueError:
            print("Ошибка: введенное значение не является числом")
