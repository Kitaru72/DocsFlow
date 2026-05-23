from app.profiles import create_student_profile


def main():
    print("DocsFlow запущен.")

    try:
        full_name = input("Введите ваше ФИО: ")
        group = input("Введите вашу группу: ")
        university = input("Введите ваш университет: ")
        faculty = input("Введите ваш факультет: ")

        student = create_student_profile(
            full_name,
            group,
            university,
            faculty,
        )
        print(student)
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
