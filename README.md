# Testosterovshiki
1. Основные ветки
main — стабильная версия, всегда в рабочем состоянии.
dev — ветка для общей интеграции фич, тестирования перед слиянием в main.

2. Фичевые ветки
Названия: feature/backend-auth, feature/frontend-navbar, bugfix/api-error, hotfix/login-crash и т.п.
Ветки создаются от dev и туда же вливаются после ревью.

3. Ветки релизов и хотфиксов (если проект большой)
release/v1.0, hotfix/v1.0.1 — удобно, если для выкатывания версии.

python 3.9.13

Запуск проекта из корня
uvicorn app.main:app --reload

Создать миграцию
alembic revision --autogenerate -m "Initial migration"

Прогнать все миграции
alembic upgrade head

Откатиться на миграцию назад
alembic downgrade -1
