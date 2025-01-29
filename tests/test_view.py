import src.view
import src.text
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("input_value", ["Message","Text"])
def test_user_input(input_value):
    """
    Тестирование функции создание контакта в модуле View
    """
    def mock_input(promt):
        return input_value

    with patch('builtins.input', mock_input):
        pb_view = src.view.PhonebookView()
        assert isinstance(pb_view.user_input(''), str)
        assert  pb_view.user_input('') == input_value

