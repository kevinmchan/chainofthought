from starlette.testclient import TestClient


def test_create_thought_endpoint(client: TestClient):
    # Create a new thought object
    data = {
        "content": "Test thought content",
        "annotations": {"tag": "test-api"},
    }

    # Call the create_thought_endpoint with the thought object
    response = client.post("/thoughts", json=data)
    response_data = response.json()

    # Assert that the response has the correct values
    assert response.status_code == 200
    assert response_data["id"] is not None
    assert response_data["created_at"] is not None
    assert response_data["current_version"] is not None
    assert response_data["current_version"]["id"] is not None
    assert response_data["current_version"]["created_at"] is not None
    assert response_data["current_version"]["thought_id"] == response_data["id"]
    assert response_data["current_version"]["content"] == data["content"]
    assert response_data["current_version"]["annotations"] == data["annotations"]
    assert response_data["current_version"]["version_number"] == 1


def test_read_thought_endpoint(client: TestClient):
    # Create a new thought object
    data = {
        "content": "Test thought content",
        "annotations": {"tag": "test-api"},
    }

    # Call the create_thought_endpoint with the thought object
    response = client.post("/thoughts", json=data)
    post_response_data = response.json()

    # Call the read_thought_endpoint with the thought ID
    response = client.get(f"/thoughts/{post_response_data['id']}")
    get_response_data = response.json()

    # Assert that the response has the correct values
    assert response.status_code == 200
    assert get_response_data == post_response_data


def test_read_nonexistent_thought(client: TestClient):
    # Call the read_thought_endpoint with a nonexistent thought ID
    response = client.get("/thoughts/-1")

    # Assert that the response has a 404 status code
    assert response.status_code == 404
    assert response.json() == {"detail": "Thought not found"}