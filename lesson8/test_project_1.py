import requests

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


def get_auth_token():
    response = requests.post(
        "https://ru.yougile.com/api-v2/auth/keys",
        json=AUTH_DATA
    )
    return response.json().get("key")


def create_project():
    response = requests.post(
        BASE_URL,
        headers=HEADERS,
        json=PROJECT_DATA
    )
    return response.json()


def get_project(project_id):
    response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS
    )
    return response.json()


def update_project(project_id, new_title):
    update_data = {"title": new_title}
    response = requests.put(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS,
        json=update_data
    )
    return response.json()


def delete_project(project_id):
    response = requests.delete(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS
    )
    return response.status_code


def test_project_lifecycle():
    # Создаем проект
    create_response = create_project()
    project_id = create_response.get("id")

    # Получаем проект и проверяем его создание
    get_response = get_project(project_id)
    assert get_response["id"] == project_id
    assert get_response["title"] == "TEST_PROJECT"

    # Обновляем проект и проверяем обновление
    updated_title = "UPDATED_TEST_PROJECT"
    update_response = update_project(project_id, updated_title)
    assert update_response["title"] == updated_title

    # Удаляем проект и проверяем удаление
    delete_status = delete_project(project_id)
    assert delete_status == 200

    # Проверяем, что проект удален (должен вернуть 404)
    check_response = requests.get(
        f"{BASE_URL}/{project_id}",
        headers=HEADERS
    )
    assert check_response.status_code == 404


if __name__ == "__main__":
    test_project_lifecycle()
