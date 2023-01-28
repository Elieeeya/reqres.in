from conftest import *


id_user = 36
a = random.randint(100, 200)
name = f'NAKA{a}'

body = {
    "name": name,
    "job": "QA AUTO Python"
}

way = f'api/users/{id_user}'


def test_patch_update_user():
    response = requests.patch(url + way, json=body)

    assert response.status_code == 200
    assert S(update_user) == response.json()
    assert response.json()['name'] == name
    assert response.json()['job'] == 'QA AUTO Python'
