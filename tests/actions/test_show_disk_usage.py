from pro_filer.actions.main_actions import show_disk_usage  # NOQA
from pro_filer.cli_helpers import _get_printable_file_path  # NOQA


def test_show_disk_usage(tmp_path, capsys):
    path_one = tmp_path / "file.txt"
    path_one.touch()

    path_two = tmp_path / "file2.txt"
    path_two.touch()

    path_one.write_text("Testando algum texto")
    path_two.write_text("Testando  algum  texto parte dois")

    context = {"all_files": [str(path_one), str(path_two)]}
    output_one = f"'{_get_printable_file_path(str(path_one))}':".ljust(70)
    output_two = f"'{_get_printable_file_path(str(path_two))}':".ljust(70)

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert (
        captured.out
        == f"{output_two} 33 (62%)\n{output_one} 20 (37%)\nTotal size: 53\n"
    )


def test_show_disk_usage_empty(capsys):
    context = {"all_files": []}
    output = "Total size: 0\n"

    show_disk_usage(context)
    captured = capsys.readouterr()
    assert output in captured.out
