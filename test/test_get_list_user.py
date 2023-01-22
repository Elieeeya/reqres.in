from conftest import *


param = {
    'page': 2
}

def test_list_user_page_response_data():
    response = requests.get(url + 'api/users', params=param)

    assert response.status_code == 200
    assert S(list_user) == response.json()
    assert response.json()['page'] == 2