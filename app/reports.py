from app.models import ReportData


def create_report_data(discipline, lab_number, topic, tasks):
    report_data = ReportData(
        discipline,
        lab_number,
        topic,
        tasks,
    )

    return report_data.to_dict()


def format_report_data(report_data, mode):
    titles = {
        "created": "Данные отчета созданы:",
        "loaded": "Данные отчета загружены:",
    }

    if mode not in titles:
        raise ValueError("Режим форматирования данных отчета указан неверно")

    title = titles[mode]
    lines = []

    lines.append(f"\n{title}")
    lines.append(f"Дисциплина: {report_data['discipline']}")
    lines.append(f"Номер лабораторной работы: {report_data['lab_number']}")
    lines.append(f"Тема лабораторной работы: {report_data['topic']}")
    lines.append("Задания:")

    for i, task in enumerate(report_data["tasks"], start=1):
        lines.append(f"Задание {i}. {task}")

    return "\n".join(lines)
