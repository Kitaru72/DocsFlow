def create_lab_report(discipline, lab_number, topic, tasks):
    if len(tasks) == 0:
        raise ValueError("Список заданий не может быть пустым")

    discipline = discipline.strip()
    lab_number = lab_number.strip()
    topic = topic.strip()
    for i in range(len(tasks)):
        tasks[i] = tasks[i].strip()

    if discipline == "":
        raise ValueError("Поле \"Дисциплина\" не может быть пустым")
    if lab_number == "":
        raise ValueError("Поле \"Номер лабораторной работы\" не может быть пустым")
    if topic == "":
        raise ValueError("Поле \"Тема лабораторной работы\" не может быть пустым")

    for i in range(len(tasks)):
        if tasks[i] == "":
            raise ValueError("Поле \"Список заданий\" не может быть пустым")

    report = {
        "discipline": discipline,
        "lab_number": lab_number,
        "topic": topic,
        "tasks": tasks,
    }

    return report


def format_lab_report(report, mode):
    titles = {
        "created": "Отчет создан:",
    }

    if mode not in titles:
        raise ValueError("Режим форматирования отчета указан неверно")

    title = titles[mode]
    lines = []

    lines.append(f"\n{title}")
    lines.append(f"Дисциплина: {report['discipline']}")
    lines.append(f"Номер лабораторной работы: {report['lab_number']}")
    lines.append(f"Тема лабораторной работы: {report['topic']}")
    lines.append("Задания:")

    for i, task in enumerate(report["tasks"], start=1):
        lines.append(f"Задание {i}. {task}")

    return "\n".join(lines)
