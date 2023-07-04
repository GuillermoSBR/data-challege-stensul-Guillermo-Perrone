from core.etl.raw_to_app import main_execution


def test_main_execution():
    result_var = main_execution()
    assert result_var == 'Hello World!'
