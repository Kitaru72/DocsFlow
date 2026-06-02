def create_profile(full_name, group, university, faculty):
    full_name = full_name.strip()
    group = group.strip()
    university = university.strip()
    faculty = faculty.strip()

    if full_name == "":
        raise ValueError("ФИО не может быть пустым")

    if group == "":
        raise ValueError("Группа не может быть пустой")

    if university == "":
        raise ValueError("Университет не может быть пустой")

    if faculty == "":
        raise ValueError("Факультет не может быть пустой")

    profile = {
        "full_name": full_name,
        "group": group,
        "university": university,
        "faculty": faculty,
    }

    return profile


def format_profile(profile, mode):
    titles = {
        "created": "Профиль создан:",
        "loaded": "Профиль загружен:",
    }

    if mode not in titles:
        raise ValueError("Выбран неверный режим форматирования профиля")

    title = titles[mode]
    profile_text = (
        f"\n{title}\n"
        f"ФИО: {profile['full_name']}\n"
        f"Группа: {profile['group']}\n"
        f"Университет: {profile['university']}\n"
        f"Факультет: {profile['faculty']}"
    )

    return profile_text
