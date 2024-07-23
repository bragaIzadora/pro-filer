import pytest
from pro_filer.actions.main_actions import find_duplicate_files  # NOQA


def test_all_files_different(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("Conteúdo do arquivo 1")

    file2 = tmp_path / "file2.txt"
    file2.write_text("Conteúdo do arquivo 2")

    all_files = [file1, file2]
    assert find_duplicate_files({"all_files": all_files}) == []


def test_all_files_equal(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("Conteúdo do arquivo")

    file2 = tmp_path / "file2.txt"
    file2.write_text("Conteúdo do arquivo")

    all_files = [file1, file2]
    assert find_duplicate_files({"all_files": all_files}) == [(file1, file2)]


def test_missing_file_raises_value_error(tmp_path):
    file1 = tmp_path / "file1.txt"
    file1.write_text("Conteúdo do arquivo 1")

    all_files = [file1, tmp_path / "file2.txt"]
    with pytest.raises(ValueError):
        find_duplicate_files({"all_files": all_files})
