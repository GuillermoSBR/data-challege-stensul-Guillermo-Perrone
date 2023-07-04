from core.etl.landing_to_raw import main_execution


def test_main_execution():
    result_var = main_execution()
    assert result_var == 'Hello World!'
