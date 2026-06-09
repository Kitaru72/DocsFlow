class ReportData:
    def __init__(self, discipline, lab_number, topic, tasks):
        if not isinstance(discipline, str):
            raise ValueError("Поле дисциплины должно быть строкой")

        if not isinstance(lab_number, str):
            raise ValueError("Поле с номером работы должно быть строкой")

        if not isinstance(topic, str):
            raise ValueError("Поле с темой работы должно быть строкой")

        if not isinstance(tasks, list):
            raise ValueError("Поле с заданиями должно быть списком")

        self.discipline = discipline.strip()
        self.lab_number = lab_number.strip()
        self.topic = topic.strip()
        self.tasks = []

        for task in tasks:
            if not isinstance(task, str):
                raise ValueError("Каждое задание должно быть строкой")

            self.tasks.append(task.strip())

        if self.discipline == "":
            raise ValueError("Поле с дисциплиной не может быть пустым")

        if self.lab_number == "":
            raise ValueError("Поле с номером работы не может быть пустым")

        if self.topic == "":
            raise ValueError("Поле с темой работы не может быть пустым")

        if len(self.tasks) < 1:
            raise ValueError("Количество заданий должно быть больше 0")

        for index, task in enumerate(self.tasks, start=1):
            if task == "":
                raise ValueError(f"Поле с заданием номер {index} не может быть пустым")

    def to_dict(self):
        return {
            "discipline": self.discipline,
            "lab_number": self.lab_number,
            "topic": self.topic,
            "tasks": self.tasks,
        }

    @classmethod
    def from_dict(cls, report_data):
        return cls(
            report_data["discipline"],
            report_data["lab_number"],
            report_data["topic"],
            report_data["tasks"],
        )
