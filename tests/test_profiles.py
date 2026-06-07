from app.profiles import create_profile


def test_create_profile_returns_valid_profile_data():
    profile = create_profile(
        "Семенов Семен Семенович",
        "8412",
        "МГТУ",
        "ИСиТ",
    )

    assert profile == {
        "full_name": "Семенов Семен Семенович",
        "group": "8412",
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }
