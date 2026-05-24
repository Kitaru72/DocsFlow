from app.profiles import create_student_profile, format_student_profile
from app.reports import create_lab_report
from app.storage import DEFAULT_PROFILE_PATH, load_student_profile, save_student_profile


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

        student_info = format_student_profile(student, "created")
        print(student_info)

        save_student_profile(student)
        print(f"\nДанные профиля студента записаны в файл {DEFAULT_PROFILE_PATH}")
        loaded_student = load_student_profile()
        loaded_student_info = format_student_profile(loaded_student, "loaded")
        print(loaded_student_info)

        discipline = input("Введите название дисциплины: ")
        lab_number = input("Введите номер лабораторной работы: ")
        topic = input("Введите тему лабораторной работы: ")

        count = int(input("Введите количество заданий: "))
        tasks = []
        for i in range(count):
            tasks.append(input(f"Введите задание номер {i+1}: "))

        report = create_lab_report(
            discipline,
            lab_number,
            topic,
            tasks,
        )

        print(report)

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
