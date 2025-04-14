# Testosterovshiki
1. Основные ветки
main — стабильная версия, всегда в рабочем состоянии.
dev — ветка для общей интеграции фич, тестирования перед слиянием в main.

2. Фичевые ветки
Названия: feature/backend-auth, feature/frontend-navbar, bugfix/api-error, hotfix/login-crash и т.п.
Ветки создаются от dev и туда же вливаются после ревью.

3. Ветки релизов и хотфиксов (если проект большой)
release/v1.0, hotfix/v1.0.1 — удобно, если для выкатывания версии.

Структура репозитория 
project/
│
├── backend/                 # Backend-часть (FastAPI)
│   ├── app/                 # Основное приложение
│   │   ├── api/             # Эндпоинты FastAPI
│   │   ├── models/          # SQLAlchemy модели
│   │   ├── schemas/         # Pydantic схемы
│   │   ├── services/        # Логика приложения
│   │   ├── db.py            # Работа с базой (инициализация, соединение)
│   │   └── main.py          # Точка входа FastAPI
│   ├── alembic/             # Миграции Alembic
│   └── alembic.ini          # Настройки Alembic
│
├── frontend/                # Статические ресурсы, если без отдельного SPA
│   ├── templates/           # HTML-файлы (Jinja2 или просто html)
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   └── index.html
│
├── ml/                      # ML-эксперименты
│   ├── notebooks/           # Jupyter notebooks
│   ├── models/              # Сохранённые модели
│   ├── preprocessing/       # Очистка и обработка данных
│   ├── training/            # Скрипты для обучения моделей
│   └── utils.py             # Вспомогательные функции
│
├── tests/                   # Тесты (pytest)
│   ├── unit/
│   └── integration/
│
├── .env                     # Переменные окружения
├── .gitignore
├── docker-compose.yml       # Описание сервисов
├── Dockerfile               # Docker для backend
├── README.md
├── requirements.txt         # Зависимости
└── setup.sh                 # Скрипт запуска/развёртывания (опционально)
