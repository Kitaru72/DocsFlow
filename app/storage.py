import json


def save_student_profile(student):
    try:
        with open("data/profile.json", "w", encoding="utf-8") as file:
            json.dump(student, file, ensure_ascii=False, indent=4)
    except OSError:
        raise ValueError("\nОшибка записи профиля студента в data/profile.json")


def load_student_profile():
    try:
        with open("data/profile.json", "r", encoding="utf-8") as file:
            output_profile = json.load(file)
    except OSError:
        raise ValueError("Файл data/profile.json отсутствует")

    return output_profile
