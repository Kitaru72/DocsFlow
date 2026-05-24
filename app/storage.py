import json


DEFAULT_PROFILE_PATH = "data/profile.json"


def save_student_profile(student, path=DEFAULT_PROFILE_PATH):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(student, file, ensure_ascii=False, indent=4)
    except OSError:
        raise ValueError(f"\nОшибка записи профиля студента в {path}")


def load_student_profile(path=DEFAULT_PROFILE_PATH):
    try:
        with open(path, "r", encoding="utf-8") as file:
            output_profile = json.load(file)
    except OSError:
        raise ValueError(f"Файл {path} отсутствует")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {path} содержит некорректный JSON")

    return output_profile
