def validate_profile_data(profile):
    if not isinstance(profile, dict):
        raise ValueError("Входные данные не являются словарем")

    required_keys = ["full_name", "group", "university", "faculty"]

    for key in required_keys:
        if key not in profile:
            raise ValueError(f"В профиле отсутствует ключ {key}")

        if not isinstance(profile[key], str):
            raise ValueError(f"Поле {key} не является строкой")

        if profile[key].strip() == "":
            raise ValueError(f"Поле {key} не может быть пустым")


def validate_report_data(report_data):
    if not isinstance(report_data, dict):
        raise ValueError("Входные данные не являются словарем")

    required_keys = ["discipline", "lab_number", "topic", "tasks"]

    for key in required_keys:
        if key not in report_data:
            raise ValueError(f"В данных отчета отсутствует ключ {key}")

    text_keys = ["discipline", "lab_number", "topic"]

    for key in text_keys:
        if not isinstance(report_data[key], str):
            raise ValueError(f"Поле {key} не является строкой")

        if report_data[key].strip() == "":
            raise ValueError(f"Поле {key} не может быть пустым")

    if not isinstance(report_data["tasks"], list):
        raise ValueError("Поле tasks не является списком")

    if len(report_data["tasks"]) == 0:
        raise ValueError("Список tasks должен содержать хотя бы 1 элемент")

    for index, task in enumerate(report_data["tasks"], start=1):
        if not isinstance(task, str):
            raise ValueError(f"Задание {index} в поле tasks должно быть строкой")

        if task.strip() == "":
            raise ValueError(f"Задание {index} в списке tasks не может быть пустым")
