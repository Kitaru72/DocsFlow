class Profile:
    def __init__(self, full_name, group, university, faculty):
        self.full_name = full_name.strip()
        self.group = group.strip()
        self.university = university.strip()
        self.faculty = faculty.strip()

        if self.full_name == "":
            raise ValueError("Поле ФИО не может быть пустым")

        if self.group == "":
            raise ValueError("Поле группа не может быть пустым")

        if self.university == "":
            raise ValueError("Поле университет не может быть пустым")

        if self.faculty == "":
            raise ValueError("Поле факультет не может быть пустым")

    def to_dict(self):
        return {
            "full_name": self.full_name,
            "group": self.group,
            "university": self.university,
            "faculty": self.faculty,
        }

    @classmethod
    def from_dict(cls, profile_data):
        return cls(
            profile_data["full_name"],
            profile_data["group"],
            profile_data["university"],
            profile_data["faculty"],
        )
