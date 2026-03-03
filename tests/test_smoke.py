from reportgen import main


def test_main_module_exists():
    assert hasattr(main, "__file__")
