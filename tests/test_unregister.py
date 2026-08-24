from src.app import activities


def test_unregister_removes_existing_participant_successfully(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = activities[activity_name]["participants"][0]
    endpoint = f"/activities/{activity_name}/participants/{participant_email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {participant_email} from {activity_name}"
    assert participant_email not in activities[activity_name]["participants"]


def test_unregister_returns_not_found_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Club"
    participant_email = "student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants/{participant_email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_returns_not_found_for_missing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    participant_email = "missing.student@mergington.edu"
    endpoint = f"/activities/{activity_name}/participants/{participant_email}"

    # Act
    response = client.delete(endpoint)

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found in this activity"
