import pytest
from users import UserTable, User


@pytest.fixture
def user_manager():
    """Фикстура для тестов - использует SQLite в памяти"""
    # Создаем чистую БД в памяти для каждого теста
    manager = UserTable(test_mode=True)

    # Добавляем начальные данные для тестов
    session = manager.Session()
    try:
        # Очищаем таблицу
        session.query(User).delete()

        # Добавляем тестовых пользователей
        test_users = [
            User(user_id=1, user_email="user1@test.com", subject_id=1),
            User(user_id=2, user_email="user2@test.com", subject_id=2),
        ]
        session.add_all(test_users)
        session.commit()
    finally:
        session.close()

    yield manager


def test_create_user(user_manager):
    """Тест создания пользователя"""
    # Act
    user_id = user_manager.create_user("new_user@yandex.ru", 5)

    # Assert
    assert user_id == 3  # Следующий ID после существующих

    user = user_manager.get_user(user_id)
    assert user is not None
    assert user.user_email == "new_user@yandex.ru"
    assert user.subject_id == 5
    assert user.is_deleted == False


def test_update_user(user_manager):
    """Тест обновления пользователя"""
    # Act
    result = user_manager.update_user(1, "updated@yandex.ru", 10)

    # Assert
    assert result == True

    user = user_manager.get_user(1)
    assert user.user_email == "updated@yandex.ru"
    assert user.subject_id == 10


def test_soft_delete_user(user_manager):
    """Тест мягкого удаления пользователя"""
    # Act
    result = user_manager.delete_user_soft(2)

    # Assert
    assert result == True

    # Пользователь не должен быть доступен через get_user
    user = user_manager.get_user(2)
    assert user is None

    # Но должен существовать в БД с флагом is_deleted
    session = user_manager.Session()
    try:
        deleted_user = session.query(User).filter(User.user_id == 2).first()
        assert deleted_user is not None
        assert deleted_user.is_deleted == True
        assert deleted_user.deleted_at is not None
    finally:
        session.close()


def test_stability_multiple_runs():
    """Тест стабильности при многократных запусках"""
    for run in range(3):
        # Создаем новый менеджер для каждого запуска
        manager = UserTable(test_mode=True)

        # Создаем пользователя
        user_id = manager.create_user(f"test{run}@yandex.ru", run)

        # Проверяем
        user = manager.get_user(user_id)
        assert user is not None
        assert user.user_email == f"test{run}@yandex.ru"

        # Обновляем
        manager.update_user(user_id, f"updated{run}@yandex.ru", run + 10)
        user = manager.get_user(user_id)
        assert user.user_email == f"updated{run}@yandex.ru"

        # Удаляем
        manager.delete_user_soft(user_id)
        user = manager.get_user(user_id)
        assert user is None
