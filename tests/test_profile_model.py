import pytest

from app.models import Profile


def test_profile_model_stores_profile_fields():
    profile = Profile(
        "Семенов Семен Семенович",
        "8412",
        "МГТУ",
        "ИСиТ",
    )

    assert profile.full_name == "Семенов Семен Семенович"
    assert profile.group == "8412"
    assert profile.university == "МГТУ"
    assert profile.faculty == "ИСиТ"


def test_profile_model_to_dict_returns_profile_data():
    profile = Profile(
        "Семенов Семен Семенович   ",
        "8412  ",
        "МГТУ",
        "ИСиТ",
    )

    profile_data = profile.to_dict()

    assert isinstance(profile_data, dict)
    assert profile_data == {
        "full_name": "Семенов Семен Семенович",
        "group": "8412",
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }


def test_profile_model_from_dict_returns_profile_object():
    profile_data = {
        "full_name": "Семенов Семен Семенович",
        "group": "8412",
        "university": "МГТУ",
        "faculty": "ИСиТ",
    }

    profile = Profile.from_dict(profile_data)

    assert isinstance(profile, Profile)
    assert profile.full_name == "Семенов Семен Семенович"
    assert profile.group == "8412"
    assert profile.university == "МГТУ"
    assert profile.faculty == "ИСиТ"


def test_profile_model_rejects_empty_name():
    with pytest.raises(ValueError):
        Profile(
            "",
            "8412",
            "МГТУ",
            "ИСиТ",
        )


def test_profile_model_rejects_empty_group():
    with pytest.raises(ValueError):
        Profile(
            "Семенов Семен Семенович",
            "",
            "МГТУ",
            "ИСиТ",
        )


def test_profile_model_rejects_empty_university():
    with pytest.raises(ValueError):
        Profile(
            "Семенов Семен Семенович",
            "8412",
            "",
            "ИСиТ",
        )


def test_profile_model_rejects_empty_faculty():
    with pytest.raises(ValueError):
        Profile(
            "Семенов Семен Семенович",
            "8412",
            "МГТУ",
            "",
        )
