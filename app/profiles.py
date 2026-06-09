from app.models import Profile


def create_profile(full_name, group, university, faculty):
    profile = Profile(
        full_name,
        group,
        university,
        faculty,
    )

    return profile.to_dict()


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
