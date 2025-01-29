import src.controller
import src.view
import src.text
import pytest
from unittest.mock import patch

@pytest.mark.parametrize("input_value", ["Test"])
def test_create_contact(input_value):
    """
    Тестирование функции создание контакта в модуле Controller
    """
    def mock_input(prompt):
        return input_value

    with patch('builtins.input', mock_input):
        result = src.controller.PhonebookController().create_contacts()
        assert isinstance(result, list)
        assert isinstance(result[0], dict)
        assert len(result[0]) == 5

