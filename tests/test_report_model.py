import pytest

from app.models import ReportData


def test_report_model_stores_report_fields():
    report = ReportData(
        "Базы данных",
        "3",
        "SELECT",
        [
            "Задание 1",
            "Задание 2",
            "Задание 3",
        ],
    )

    assert report.discipline == "Базы данных"
    assert report.lab_number == "3"
    assert report.topic == "SELECT"
    assert report.tasks == ["Задание 1", "Задание 2", "Задание 3"]


def test_report_model_strips_text_fields():
    report = ReportData(
        "  Базы данных  ",
        "  3  ",
        "  SELECT  ",
        [
            "  Задание 1  ",
            "  Задание 2  ",
            "  Задание 3  ",
        ],
    )

    assert report.discipline == "Базы данных"
    assert report.lab_number == "3"
    assert report.topic == "SELECT"
    assert report.tasks == ["Задание 1", "Задание 2", "Задание 3"]


def test_report_model_to_dict_returns_report_data():
    report = ReportData(
        "Базы данных",
        "3",
        "SELECT",
        [
            "Задание 1",
            "Задание 2",
            "Задание 3",
        ],
    )

    report_data = report.to_dict()

    assert report_data == {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3",
        ],
    }


def test_report_model_from_dict_returns_report_object():
    report_data = {
        "discipline": "Базы данных",
        "lab_number": "3",
        "topic": "SELECT",
        "tasks": [
            "Задание 1",
            "Задание 2",
            "Задание 3",
        ],
    }

    report = ReportData.from_dict(report_data)

    assert isinstance(report, ReportData)
    assert report.discipline == "Базы данных"
    assert report.lab_number == "3"
    assert report.topic == "SELECT"
    assert report.tasks == ["Задание 1", "Задание 2", "Задание 3"]


def test_report_model_rejects_non_string_field():
    with pytest.raises(ValueError):
        ReportData(
            "Базы данных",
            3,
            "SELECT",
            [
                "Задание 1",
                "Задание 2",
                "Задание 3",
            ],
        )


def test_report_model_rejects_non_list_tasks():
    with pytest.raises(ValueError):
        ReportData(
            "Базы данных",
            "3",
            "SELECT",
            (
                "Задание 1",
                "Задание 2",
                "Задание 3",
            ),
        )


def test_report_model_rejects_non_string_task():
    with pytest.raises(ValueError):
        ReportData(
            "Базы данных",
            "3",
            "SELECT",
            [
                123,
                "Задание 2",
                "Задание 3",
            ],
        )


def test_report_model_rejects_empty_task():
    with pytest.raises(ValueError):
        ReportData(
            "Базы данных",
            "3",
            "SELECT",
            [
                "",
                "Задание 2",
                "Задание 3",
            ],
        )


def test_report_model_rejects_empty_tasks():
    with pytest.raises(ValueError):
        ReportData(
            "Базы данных",
            "3",
            "SELECT",
            [],
        )
