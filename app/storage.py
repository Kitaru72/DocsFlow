import json


PROFILE_PATH = "data/profile.json"
REPORT_PATH = "data/report.json"


def save_json(data, path):
    try:
        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        raise ValueError(f"\nОшибка записи JSON в {path}")


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except OSError:
        raise ValueError(f"Файл {path} отсутствует")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {path} содержит некорректный JSON")

    return data


def save_student_profile(student, path=PROFILE_PATH):
    save_json(student, path)


def load_student_profile(path=PROFILE_PATH):
    return load_json(path)


def save_lab_report(report, path=REPORT_PATH):
    save_json(report, path)


def load_lab_report(path=REPORT_PATH):
    return load_json(path)
