from sqlalchemy import create_engine, Column, Integer, String, Boolean, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# Исправленный импорт для SQLAlchemy 2.0+
Base = declarative_base()


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_email = Column(String(100), nullable=False)
    subject_id = Column(Integer, nullable=False)
    is_deleted = Column(Boolean, default=False)
    deleted_at = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)


class UserTable:
    def __init__(self, test_mode=False):
        if test_mode:
            # Используем SQLite в памяти для тестов
            self.engine = create_engine('sqlite:///:memory:')
            Base.metadata.create_all(self.engine)
        else:
            # Для продакшена - ваша реальная БД
            self.engine = create_engine("postgresql://postgres:E2eqefd@localhost:5432/QA")

        self.Session = sessionmaker(bind=self.engine)

    def create_user(self, user_email, subject_id):
        session = self.Session()
        try:
            # Находим максимальный ID
            max_user = session.query(User).order_by(User.user_id.desc()).first()
            new_user_id = max_user.user_id + 1 if max_user else 1

            new_user = User(
                user_id=new_user_id,
                user_email=user_email,
                subject_id=subject_id
            )
            session.add(new_user)
            session.commit()
            return new_user_id
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def get_user(self, user_id):
        session = self.Session()
        try:
            return session.query(User).filter(
                User.user_id == user_id,
                User.is_deleted == False
            ).first()
        finally:
            session.close()

    def get_all_users(self):
        session = self.Session()
        try:
            return session.query(User).filter(User.is_deleted == False).all()
        finally:
            session.close()

    def update_user(self, user_id, user_email, subject_id):
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user:
                user.user_email = user_email
                user.subject_id = subject_id
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

    def delete_user_soft(self, user_id):
        """Мягкое удаление"""
        session = self.Session()
        try:
            user = session.query(User).filter(User.user_id == user_id).first()
            if user:
                user.is_deleted = True
                user.deleted_at = datetime.now()
                session.commit()
                return True
            return False
        except Exception as e:
            session.rollback()
            raise e
        finally:
            session.close()

