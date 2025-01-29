import src.controller
import src.view
import src.text
import src.text
from src import view
from src.model import PhonebookModel


def test_show_all_contacts():
    result = PhonebookModel(src.text.PATH)
    assert isinstance(result.read_file(), list)

