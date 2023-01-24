from conftest import *


def test_get_single_resource_response_page_data():
    response = requests.get(url + 'api/unknown/2')

    assert response.status_code == 200
    assert S(single_resource) == response.json()

    assert response.json()['data']['id'] == 2
    assert response.json()['data']['name'] == 'fuchsia rose'
    assert response.json()['data']['year'] == 2001
    assert response.json()['data']['color'] == '#C74375'
    assert response.json()['data']['pantone_value'] == '17-2031'