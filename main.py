from app.profiles import create_student_profile


def main():
    print("DocsFlow запущен.")

    try:
        student = create_student_profile(
            "Колесниченко Иван Александрович   ",
            "3403  ",
            "НВГУ",
            "ИСиТ",
        )
        print(student)
    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
