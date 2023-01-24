from conftest import *


def test_get_single_resource_found_response_user_id_23():
    response = requests.get(url + 'api/users/23')

    assert response.status_code == 404
    assert response.json() == {}