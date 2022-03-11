import pytest
# from ../code import main_program

@pytest.fixture(scope="module")
def get_temp_data():
    return '../code/temp_data'

class Flag:

