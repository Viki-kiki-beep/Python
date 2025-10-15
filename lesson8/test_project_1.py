import requests
import pytest

TOKEN = ""
BASE_URL = "https://ru.yougile.com/api-v2/projects"

HEADERS = {
    "Authorization": f'Bearer {TOKEN}',
    "Content-Type": 'application/json'
}

AUTH_DATA = {
    "login": "",
    "password": "",
    "companyId": ""
}

PROJECT_DATA = {
    "title": "TEST_PROJECT",
    "users": {
        "846dc855-1eff-41ba-a908-06f1d9f0c985": "admin"
    }
}


def test_add_project():
    response = requests.post(BASE_URL, json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 201
    project_id = response.json().get('id')
    assert project_id is not None
    print(f"Project ID: {project_id}")
    return project_id
def test_list_projects():
    response = requests.get(BASE_URL, headers=HEADERS)
    assert response.status_code == 200
    projects = response.json()
    return projects
def test_get_project():
    project_id = test_add_project()
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 200
    project_data = response.json()
    assert project_data.get('id') == project_id
def test_update_project():
    project_id = test_add_project()
    update_data = {
        "deleted": True,
        "title": "Updated Title",
        "users": {
            "846dc855-1eff-41ba-a908-06f1d9f0c985": "admin"
        }
    }
    response = requests.put(f"{BASE_URL}/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 200
def test_add_project_noname():
    PROJECT_DATA={
    "title": "",
    "users": {
        "846dc855-1eff-41ba-a908-06f1d9f0c985": "admin"
    }
}
    response = requests.post(BASE_URL, json=PROJECT_DATA, headers=HEADERS)
    assert response.status_code == 400
def test_get_project_error_id():
    project_id="error"
    response = requests.get(f"{BASE_URL}/{project_id}", headers=HEADERS)
    assert response.status_code == 404
def test_update_baddate_project():
    project_id = test_add_project()
    update_data = {
        "deleted": False,
        "title": "Updated Title",
        "users": {
            "846dc855-1eff-41ba-a908-06f1d9f0c985": "error"
        }
    }
    response = requests.put(f"{BASE_URL}/{project_id}", json=update_data, headers=HEADERS)
    assert response.status_code == 400
