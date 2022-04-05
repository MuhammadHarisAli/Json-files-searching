from pathlib import Path
import exercise


def test_user_file_exist():
    path_to_file = './users.json'
    path = Path(path_to_file)
    assert True == path.is_file()


def test_ticket_file_exist():
    path_to_file = './tickets.json'
    path = Path(path_to_file)
    assert True == path.is_file()


def test_organization_file_exist():
    path_to_file = './organizations.json'
    path = Path(path_to_file)
    assert True == path.is_file()


def test_constructor_user_data_object():
    obj = exercise.Search()
    assert True == bool(obj.data_user)


def test_constructor_data_ticket_object():
    obj = exercise.Search()
    assert True == bool(obj.data_ticket)


def test_constructor_data_organization_object():
    obj = exercise.Search()
    assert True == bool(obj.data_organization)