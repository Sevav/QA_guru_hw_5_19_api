import requests


def test_create_user():
    name = "Ilon Mask"
    job = "Space"

    response = requests.post(
        url='https://reqres.in/api/users',
        json={
            "name": name,
            "job": job}
    )

    assert response.status_code == 201
    assert response.json()['name'] == name
    assert response.json()['job'] == job


def test_delete_user():
    response = requests.delete(url='https://reqres.in/api/users/2')

    assert response.status_code == 204
    assert response.text == ''


def test_login_successful():
    email = "eve.holt@reqres.in"
    password = "cityslicka"

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": email,
            "password": password}
    )

    assert response.status_code == 200
    assert response.json()['token'] != ''


def test_login_unsuccessful():
    email = "a1@a1"

    response = requests.post(
        url='https://reqres.in/api/login',
        json={
            "email": email}
    )

    assert response.status_code == 400
    assert response.json()['error'] == 'Missing password'


def test_single_user_not_found():
    response = requests.get(url='https://reqres.in/api/users/33')

    assert response.status_code == 404
    assert response.text == '{}'


def test_total_users():
    users_count = 12
    page = 2

    response = requests.get('https://reqres.in/api/users', params={'page': page})

    assert response.json()['total'] == users_count
    assert response.status_code == 200


def test_register_successful():
    email = "eve.holt@reqres.in"
    password = "pistole"

    response = requests.post(url='https://reqres.in/api/register',
                             json={
                                 "email": email,
                                 "password": password}
                             )

    assert response.status_code == 200
    assert response.json()['id'] != ''


def test_register_unsuccessful():
    email = "sydney@fife"

    response = requests.post(url='https://reqres.in/api/register', json={"email": email})

    assert response.status_code == 400
    assert response.json()["error"] == "Missing password"


def test_update_user_info():
    res = requests.patch('https://reqres.in/api/users/2', json={
        "name": "morpheus",
        "job": "zion resident"
    })

    assert res.status_code == 200
    assert res.json()["job"] == 'zion resident'


def test_users_length():
    users_count = 6

    response = requests.get('https://reqres.in/api/users')

    assert len(response.json()['data']) == users_count

