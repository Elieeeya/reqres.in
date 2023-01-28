from conftest import *

body = {
    "name": "NAKAMA",
    "job": "QA AUTO"
}


def test_put_update_user():
    response = requests.put(url + 'api/users/446', json=body)

    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()['name'] == 'NAKAMA'
    assert response.json()['job'] == 'QA AUTO'
