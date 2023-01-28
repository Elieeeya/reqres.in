from conftest import *


id_user = 2

way = f'api/users/{id_user}'

def test_delete_delete_user():
    response = requests.delete(url + way)

    assert response.status_code == 204
