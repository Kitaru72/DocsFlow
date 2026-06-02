from app.storage import (
    search_files,
    load_profile,
    PROFILE_DIR,
    REPORT_DIR,
    load_report_data,
    save_profile,
    create_profile_path,
    create_report_data_path,
    save_report_data,
)

from app.profiles import (
    format_profile,
    create_profile,
)

from app.reports import (
    format_report_data,
    create_report_data,
)

from app.docx_generator import (
    create_document_data,
    save_docx,
    create_docx_path
)


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


def show_menu():
    print(
            "\nDocsFlow запущен.\n",
            "1. Создать профиль\n",
            "2. Загрузить профиль\n",
            "3. Создать данные отчета\n",
            "4. Загрузить данные отчета\n",
            "5. Сгенерировать DOCX-отчет\n",
            "0. Выйти\n",
        )


def create_profile_flow():
    full_name, group, university, faculty = ask_profile_data()
    profile = create_profile(full_name, group, university, faculty)

    path = create_profile_path(profile)
    save_profile(profile, path)

    profile_info = format_profile(profile, "created")
    print(profile_info)


def create_report_data_flow():
    discipline, lab_number, topic, tasks = ask_report_data()
    report_data = create_report_data(discipline, lab_number, topic, tasks)

    path = create_report_data_path(report_data)
    save_report_data(report_data, path)

    report_data_info = format_report_data(report_data, "created")
    print(report_data_info)


def load_profile_flow():
    profile_paths = search_files(PROFILE_DIR, "json")

    if len(profile_paths) == 0:
        print("Профили не найдены")
        return None

    show_profiles(profile_paths)
    selected_path = choice_file(profile_paths)

    profile = load_profile(selected_path)
    profile_info = format_profile(profile, "loaded")
    print(profile_info)

    return profile


def load_report_data_flow():
    report_data_paths = search_files(REPORT_DIR, "json")

    if len(report_data_paths) == 0:
        print("Данные отчетов не найдены")
        return None

    show_report_data_list(report_data_paths)
    selected_report_data_path = choice_file(report_data_paths)

    report_data = load_report_data(selected_report_data_path)
    report_data_info = format_report_data(report_data, "loaded")
    print(report_data_info)

    return report_data


def generate_docx_flow():
    print("Выберите профиль для генерации DOCX-отчета: ")
    profile = load_profile_flow()
    if profile is None:
        return

    print("Выберите данные отчета для генерации DOCX-отчета: ")
    report_data = load_report_data_flow()
    if report_data is None:
        return

    document_data = create_document_data(profile, report_data)
    docx_path = create_docx_path(document_data)

    saved_docx_path = save_docx(document_data, docx_path)
    print(f"Документ сохранен: {saved_docx_path}")


def ask_profile_data():
    full_name = input("Введите ваше ФИО: ")
    group = input("Введите вашу группу: ")
    university = input("Введите ваш университет: ")
    faculty = input("Введите ваш факультет: ")

    return (full_name, group, university, faculty)


def ask_report_data():
    discipline = input("\nВведите название дисциплины: ")
    lab_number = input("Введите номер лабораторной работы: ")
    topic = input("Введите тему лабораторной работы: ")
    count = ask_positive_int("Введите количество заданий: ")

    tasks = []
    for i in range(count):
        tasks.append(input(f"Введите задание номер {i+1}: "))

    return discipline, lab_number, topic, tasks


def choice_file(file_paths):

    while True:
        choice = ask_positive_int("Выберите номер: ")

        if 1 <= choice <= len(file_paths):
            return file_paths[choice - 1]

        print(f"Ошибка! Введите число от 1 до {len(file_paths)}")


def show_profiles(profile_paths):
    for index, path in enumerate(profile_paths, start=1):
        profile = load_profile(path)
        full_name = profile["full_name"]
        group = profile["group"]

        print(f"{index}. {full_name}, группа {group}")


def show_report_data_list(report_data_paths):
    for index, path in enumerate(report_data_paths, start=1):
        report_data = load_report_data(path)
        discipline = report_data["discipline"]
        topic = report_data["topic"]
        lab_number = report_data["lab_number"]

        print(f"{index}. {discipline}: {topic}. Лаб.{lab_number}")


def run_cli():
    while True:
        show_menu()
        choice = input("Выберите действие: ").strip()
        try:
            match choice:
                case "1":
                    create_profile_flow()
                case "2":
                    load_profile_flow()
                case "3":
                    create_report_data_flow()
                case "4":
                    load_report_data_flow()
                case "5":
                    generate_docx_flow()
                case "0":
                    break
                case _:
                    print("Ошибка: выберите пункт меню от 0 до 5")

        except ValueError as error:
            print(f"Ошибка: {error}")
