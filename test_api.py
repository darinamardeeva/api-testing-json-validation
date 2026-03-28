import requests

BASE_URL = "https://jsonplaceholder.typicode.com"


def test_status_code():
    response = requests.get(f"{BASE_URL}/posts")
    assert response.status_code == 200


def test_response_type():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    assert isinstance(data, list)


def test_json_structure():
    response = requests.get(f"{BASE_URL}/posts")
    data = response.json()

    post = data[0]

    assert "userId" in post
    assert "id" in post
    assert "title" in post
    assert "body" in post


def test_data_types():
    response = requests.get(f"{BASE_URL}/posts")
    post = response.json()[0]

    assert isinstance(post["userId"], int)
    assert isinstance(post["id"], int)
    assert isinstance(post["title"], str)
    assert isinstance(post["body"], str)


def test_create_post():
    payload = {
        "title": "test",
        "body": "test body",
        "userId": 1
    }

    response = requests.post(f"{BASE_URL}/posts", json=payload)

    assert response.status_code == 201
    assert response.json()["title"] == "test"
