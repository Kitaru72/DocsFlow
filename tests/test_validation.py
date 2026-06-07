import pytest
from app.validation import validate_profile_data, validate_report_data


def test_validate_report_data_rejects_empty_field():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "",
        "topic": "SELECT",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ],
    }

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_report_data_rejects_empty_task():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            "",
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ],
    }

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_report_data_rejects_non_dict():
    report_data = [
        "Базы данных",
        "3",
        "SELECT",
        ["Задание 1", "Задание 2", "Задание 3"],
    ]

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_report_data_rejects_non_string_task():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            123,
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ],
    }

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_report_data_rejects_tasks_list_type():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": (
            "Задание 1",
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ),
    }

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_report_data_rejects_missing_key():
    report_data = {
        "discipline": "Базы данных",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ],
    }

    with pytest.raises(ValueError):
        validate_report_data(report_data)


def test_validate_profile_data_rejects_non_string():
    profile_data = {
        "full_name": "Янков Андрей Алексеевич",
        "group": 541,
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }

    with pytest.raises(ValueError):
        validate_profile_data(profile_data)


def test_validate_profile_data_rejects_non_dict():
    profile_data = ["Янков Андрей Алексеевич", "541", "МГТУ", "ИСиТ"]

    with pytest.raises(ValueError):
        validate_profile_data(profile_data)


def test_validate_profile_data_rejects_empty_field():
    profile_data = {
        "full_name": "Янков Андрей Алексеевич",
        "group": "",
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }

    with pytest.raises(ValueError):
        validate_profile_data(profile_data)


def test_validate_profile_data_accepts_valid_profile_data():
    profile_data = {
        "full_name": "Янков Андрей Алексеевич",
        "group": "541",
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }

    validate_profile_data(profile_data)


def test_validate_report_data_accepts_valid_report_data():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3",
            "Задание 4",
            "Задание 5",
        ],
    }

    validate_report_data(report_data)
