import json
from pathlib import Path


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
    save_json(profile, path)


def load_profile(path):
    return load_json(path)


def save_report_data(report, path):
    save_json(report, path)


def load_report_data(path):
    return load_json(path)


def search_files(directory, extension):
    directory_path = Path(directory)
    files = list(directory_path.glob(f"*.{extension}"))
    return files


def create_profile_path(profile):
    full_name = profile["full_name"]
    group = profile["group"]

    filename = f"{full_name}. Группа {group}.json"

    return Path(PROFILE_DIR / filename)


def create_report_data_path(report_data):
    discipline = report_data["discipline"]
    lab_number = report_data["lab_number"]
    topic = report_data["topic"]

    filename = f"{discipline}. {topic}. Лаб.{lab_number}.json"

    return Path(REPORT_DIR / filename)
