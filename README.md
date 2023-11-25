# FastAPI Learning Project

## Обзор
Этот пет-проект демонстрирует навыки разработки API с использованием технологии FastAPI. 

## Цель и задачи проекта
Цель проекта - реализовать базовый функционал интернет магазина. 
Функционал включает:
- Аутентификацию и авторизацию пользователей;
- Инструменты управления товарами;
- Функционал создания заказа пользователем;
- Базовый пользовательский интерфейс.

## Реализованно:
- **API**: Структурированные маршруты и эндпоинты API с использованием FastAPI;
- **CRUD**: Операции создания, чтения, обновления и удаления записей;
- **Модели базы данных**: Созданы модели базы данных с помощью SQLAlchemy;
- **Валидация данных**: Pydantic схемы для проверки данных запросов и ответов;
- **Бизнес логика**: Сервисный уровень для инкапсуляции бизнес-логики;
- **Аутентификация и авторизация**: Управление аутентификацией пользователей и контролем доступа на основе ролей;
- **Миграции**: Использование технологии миграции базы данных alembic;
- **Testing**: Unit тестирование функций с использованием pytest;
- **Exception Handling**: Обработка пользовательских исключений.

## Развертывание

### Необходимые технологии
- Docker
- Python 3.11+

### Установка и настройка
1. **Клонировать репозиторий**
   ```bash
   git clone https://github.com/denis-kosobanov/fastApi-learn.git
   cd fastApi-learn

2. **Запуск Docker**
   ```bash
   docker-compose up --build
   
2. **Установить зависимости**
   ```bash
   pip install -r requirements.txt

3. **Инициализировать данные**
   ```bash
   python app/initial_data.py
   
4. **Запуск приложения**
   ```bash
   uvicorn app.main:app --reload

## Схема базы данных

![data base schema](docs/db_schema.png)

## Документация API

После запуска приложения http://127.0.0.1:8000/docs

![data base schema](docs/api_docs.png)
![data base schema](docs/api_docs2.png)

## Contact
Denis Kosobanov

Email: kosobanovden@mail.ru

Project Link: https://github.com/denis-kosobanov/fastApi-learn