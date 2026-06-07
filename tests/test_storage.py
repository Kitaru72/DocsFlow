from app.storage import sanitize_filename


def test_sanitize_filename_removes_forbidden_chars():
    result = sanitize_filename("\\Коле*сниче|нко*_3403?_лаб5   * ")

    assert result == "Колесниченко_3403_лаб5"
