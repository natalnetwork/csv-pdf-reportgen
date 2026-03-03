def test_import_package():
    import reportgen  # noqa: F401


def test_import_cli_and_pipeline():
    from reportgen import cli, pipeline  # noqa: F401
