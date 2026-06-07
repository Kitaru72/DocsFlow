import pytest

from app.reports import create_report_data


def test_create_report_data_returns_valid_report_data():
    report_data = create_report_data(
        "Базы данных",
        "3",
        "SELECT",
        [
            "Задание 1",
            "Задание 2",
            "Задание 3",
        ],
    )

    assert report_data == {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3"
        ],
    }


def test_create_report_data_strips_text_fields():
    report_data = create_report_data(
        "  Базы данных   ",
        " 3  ",
        "  SELECT ",
        [
            "   Задание 1  ",
            "  Задание 2  ",
            "  Задание 3 ",
        ],
    )

    assert report_data["discipline"] == "Базы данных"
    assert report_data["lab_number"] == "3"
    assert report_data["topic"] == "SELECT"
    assert report_data["tasks"][0] == "Задание 1"
    assert report_data["tasks"][1] == "Задание 2"
    assert report_data["tasks"][2] == "Задание 3"


def test_create_report_data_rejects_empty_tasks():
    with pytest.raises(ValueError):
        create_report_data(
            "Базы данных",
            "3",
            "SELECT",
            [],
        )


def test_create_report_data_rejects_empty_task():
    with pytest.raises(ValueError):
        create_report_data(
            "Базы данных",
            "3",
            "SELECT",
            [
                "Задание 1",
                "",
            ],
        )


def test_create_report_data_rejects_empty_field():
    with pytest.raises(ValueError):
        create_report_data(
            "Базы данных",
            "",
            "SELECT",
            [
                "Задание 1",
                "Задание 2",
            ],
        )
