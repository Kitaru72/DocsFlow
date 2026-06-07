import json
from pathlib import Path

from app.validation import validate_profile_data, validate_report_data


PROFILE_DIR = Path("data/profiles")
REPORT_DIR = Path("data/reports")


def save_json(data, path):
    file_path = Path(path)
    try:
        file_path.parent.mkdir(parents=True, exist_ok=True)
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)
    except OSError:
        raise ValueError(f"\nОшибка записи JSON в {file_path}")


def load_json(path):
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
    except OSError:
        raise ValueError(f"Файл {path} отсутствует")
    except json.JSONDecodeError:
        raise ValueError(f"Файл {path} содержит некорректный JSON")

    return data


def save_profile(profile, path):
    validate_profile_data(profile)
    save_json(profile, path)


def load_profile(path):
    profile = load_json(path)
    validate_profile_data(profile)
    return profile


def save_report_data(report_data, path):
    validate_report_data(report_data)
    save_json(report_data, path)


def load_report_data(path):
    report_data = load_json(path)
    validate_report_data(report_data)
    return report_data


def search_files(directory, extension):
    directory_path = Path(directory)
    files = list(directory_path.glob(f"*.{extension}"))
    return files


def create_profile_path(profile):
    full_name = profile["full_name"]
    group = profile["group"]

    filename = f"{full_name}. Группа {group}.json"
    formatted_filename = sanitize_filename(filename)

    return Path(PROFILE_DIR / formatted_filename)


def create_report_data_path(report_data):
    discipline = report_data["discipline"]
    lab_number = report_data["lab_number"]
    topic = report_data["topic"]

    filename = f"{discipline}. {topic}. Лаб.{lab_number}.json"
    formatted_filename = sanitize_filename(filename)

    return Path(REPORT_DIR / formatted_filename)


def sanitize_filename(filename):
    forbidden_chars = ["\\", "/", ":", "*", "?", '"', "<", ">", "|"]

    for char in forbidden_chars:
        filename = filename.replace(char, "")

    formatted_filename = " ".join(filename.split())
    return formatted_filename
