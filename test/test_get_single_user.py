from conftest import *



def test_get_single_user_data_response_user_id_2():
    response = requests.get(url + 'api/users/2')

    assert response.status_code == 200
    assert S(single_user) == response.json()

    assert response.json()['data']['id'] == 2
    assert response.json()['data']['email'] == 'janet.weaver@reqres.in'
    assert response.json()['data']['first_name'] == 'Janet'
    assert response.json()['data']['last_name'] == 'Weaver'
    assert response.json()['data']['avatar'] == 'https://reqres.in/img/faces/2-image.jpg'