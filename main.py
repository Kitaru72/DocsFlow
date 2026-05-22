from app.profiles import create_student_profile


def main():
    print("DocsFlow запущен.")

    student = create_student_profile(
        "Колесниченко Иван Александрович",
        "3403",
        "НВГУ",
        "ИСиТ",
    )
    print(student)


if __name__ == "__main__":
    main()
