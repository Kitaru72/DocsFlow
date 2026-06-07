import pytest

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


def test_create_profile_rejects_empty_full_name():
    with pytest.raises(ValueError):
        create_profile(
            "",
            "5126",
            "МГТУ",
            "ИСиТ",
        )


def test_create_profile_rejects_empty_group():
    with pytest.raises(ValueError):
        create_profile(
            "Семенов Семен Семенович",
            "",
            "МГТУ",
            "ИСиТ",
        )


def test_create_profile_rejects_empty_university():
    with pytest.raises(ValueError):
        create_profile(
            "Семенов Семен Семенович",
            "5126",
            "",
            "ИСиТ",
        )


def test_create_profile_rejects_empty_faculty():
    with pytest.raises(ValueError):
        create_profile(
            "Семенов Семен Семенович",
            "5126",
            "МГТУ",
            "",
        )


def test_create_profile_strips_text_fields():
    profile = create_profile(
        "   Семенов Семен Семенович    ",
        "   8412  ",
        "   МГТУ        ",
        "     ИСиТ  ",
    )

    assert profile["full_name"] == "Семенов Семен Семенович"
    assert profile["group"] == "8412"
    assert profile["university"] == "МГТУ"
    assert profile["faculty"] == "ИСиТ"
