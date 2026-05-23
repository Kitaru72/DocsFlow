def create_student_profile(full_name, group, university, faculty):
    full_name = full_name.strip()
    group = group.strip()
    university = university.strip()
    faculty = faculty.strip()

    if full_name == "":
        raise ValueError("ФИО не может быть пустым")

    if group == "":
        raise ValueError("Группа не может быть пустой")

    if university == "":
        raise ValueError("Университет не может быть пустой")

    if faculty == "":
        raise ValueError("Факультет не может быть пустой")

    student = {
        "full_name": full_name,
        "group": group,
        "university": university,
        "faculty": faculty,
    }

    return student


def format_student_profile(student):
    profile_text = (
        "\nПрофиль студента создан:\n"
        f"ФИО: {student['full_name']}\n"
        f"Группа: {student['group']}\n"
        f"Университет: {student['university']}\n"
        f"Факультет: {student['faculty']}\n"
    )

    return profile_text
