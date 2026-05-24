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
