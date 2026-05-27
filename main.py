from app.cli import ask_positive_int
from app.profiles import create_student_profile, format_student_profile
from app.reports import create_lab_report, format_lab_report
from app.storage import (
    PROFILE_PATH,
    REPORT_PATH,
    load_lab_report,
    load_student_profile,
    save_lab_report,
    save_student_profile,
)


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
        print(f"\nДанные профиля студента записаны в файл {PROFILE_PATH}")
        loaded_student = load_student_profile()
        loaded_student_info = format_student_profile(loaded_student, "loaded")
        print(loaded_student_info)

        discipline = input("\nВведите название дисциплины: ")
        lab_number = input("Введите номер лабораторной работы: ")
        topic = input("Введите тему лабораторной работы: ")
        count = ask_positive_int("Введите количество заданий: ")

        tasks = []
        for i in range(count):
            tasks.append(input(f"Введите задание номер {i+1}: "))

        report = create_lab_report(
            discipline,
            lab_number,
            topic,
            tasks,
        )
        save_lab_report(report)
        print(f"\nДанные отчета записаны в файл {REPORT_PATH}")

        loaded_report = load_lab_report()
        loaded_report_info = format_lab_report(loaded_report, "loaded")
        print(loaded_report_info)

    except ValueError as error:
        print(f"Ошибка: {error}")


if __name__ == "__main__":
    main()
