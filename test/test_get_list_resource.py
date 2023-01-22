from conftest import *


def test_get_list_resource_response_page_1_data():
    response = requests.get(url + 'api/unknown')

    assert response.status_code == 200
    assert S(list_resource) == response.json()

    assert response.json()['data'][0]['id'] == 1
    assert response.json()['data'][1]['name'] == 'fuchsia rose'
    assert response.json()['data'][2]['year'] == 2002
    assert response.json()['data'][3]['color'] == '#7BC4C4'
    assert response.json()['data'][4]['pantone_value'] == '17-1456'