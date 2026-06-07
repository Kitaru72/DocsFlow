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
