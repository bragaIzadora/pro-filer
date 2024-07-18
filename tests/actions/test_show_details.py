import os
from datetime import datetime
from pro_filer.actions.main_actions import show_details  # NOQA


def test_show_details_existing_file(tmp_path, capsys):
    file_path = tmp_path / "Trybe_logo.png"
    file_path.write_text("some content")

    mod_time = datetime(2023, 6, 13).timestamp()
    os.utime(file_path, (mod_time, mod_time))

    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        f"File name: Trybe_logo.png\n"
        f"File size in bytes: {file_path.stat().st_size}\n"
        "File type: file\n"
        "File extension: .png\n"
        "Last modified date: 2023-06-13\n"
    )
    assert captured.out == expected_output


def test_show_details_non_existing_file(capsys):
    context = {"base_path": "/non/existing/path"}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = "File 'path' does not exist\n"
    assert captured.out == expected_output


def test_show_details_directory(tmp_path, capsys):
    dir_path = tmp_path / "Downloads"
    dir_path.mkdir()

    mod_time = datetime(2023, 6, 13).timestamp()
    os.utime(dir_path, (mod_time, mod_time))

    context = {"base_path": str(dir_path)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: Downloads\n"
        f"File size in bytes: {dir_path.stat().st_size}\n"
        "File type: directory\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-06-13\n"
    )
    assert captured.out == expected_output


def test_show_details_file_no_extension(tmp_path, capsys):
    file_path = tmp_path / "file_without_extension"
    file_path.write_text("some content")

    mod_time = datetime(2023, 6, 13).timestamp()
    os.utime(file_path, (mod_time, mod_time))

    context = {"base_path": str(file_path)}
    show_details(context)
    captured = capsys.readouterr()
    expected_output = (
        "File name: file_without_extension\n"
        f"File size in bytes: {file_path.stat().st_size}\n"
        "File type: file\n"
        "File extension: [no extension]\n"
        "Last modified date: 2023-06-13\n"
    )
    assert captured.out == expected_output
