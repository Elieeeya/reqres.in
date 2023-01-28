from conftest import *

a = random.randint(0, 100)
name = f'Vavava{a}'

body = {
    "name": name,
    "job": "QA"
}


def test_post_create_user():
    response = requests.post(url + 'api/users', json=body)

    assert response.status_code == 201
    assert S(create_user) == response.json()
    assert response.json()['name'] == name
    assert response.json()['job'] == 'QA'
    user_id = response.json()['id']
    print(f'Твой id {user_id}')

