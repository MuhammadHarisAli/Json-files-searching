from pathlib import Path
def test_user_file_exist():
    path_to_file = '/Users/muhammadharis/Desktop/coding-exercise/users.json'
    path = Path(path_to_file)
    assert True == path.is_file()


def test_ticket_file_exist():
    path_to_file = '/Users/muhammadharis/Desktop/coding-exercise/tickets.json'
    path = Path(path_to_file)
    assert True == path.is_file()


def test_organization_file_exist():
    path_to_file = '/Users/muhammadharis/Desktop/coding-exercise/organizations.json'
    path = Path(path_to_file)
    assert True == path.is_file()