# Решение тестового задания для позиции Junior Backend Developer
Проект представляет собой систему управления заказами в кафе с веб-интерфейсом и REST API.
## Описание 📝
Проект "Cafe Orders" позволяет управлять заказами в кафе, включая создание, редактирование, удаление и просмотр заказов, а также расчет выручки. Основные функции включают:
Хранение информации о заказах (номер стола, список блюд, общая стоимость, статус).

- Веб-интерфейс для CRUD-операций (создание, чтение, обновление, удаление)

- REST API для взаимодействия с системой через HTTP-запросы

- Поиск и фильтрация заказов по номеру стола и статусу

- Расчет общей выручки по оплаченным заказам

## Установка 
Для запуска проекта выполните следующие шаги:
- Клонируйте репозиторий:
```
git clone https://github.com/meloch287/Internship-effective-mobile.git
```
- Перейдите в директорию проекта:
  
```
cd Internship-effective-mobile
```

- Установите зависимости из файла requirements.txt:
  
```
pip install -r requirements.txt
```

- Настройте базу данных (по умолчанию используется SQLite, но можно переключиться на PostgreSQL в settings.py).

- Выполните миграции:
  
```
python manage.py migrate
```
- Запустите сервер разработки:

```
python manage.py runserver
```

- Проект будет доступен по адресу http://127.0.0.1:8000/.
  
## Использование ☀️
### Веб-интерфейс

- Список заказов: Отображает все заказы с возможностью фильтрации по номеру стола или статусу ("в ожидании", "готово", "оплачено").

- Создание заказа: Форма для добавления нового заказа с указанием номера стола и списка блюд.

- Редактирование и удаление: Страницы для изменения деталей заказа или его удаления.

- Изменение статуса: Интерфейс для обновления статуса заказа (например, с "в ожидании" на "оплачено").

- Расчет выручки: Отдельная страница, показывающая общую сумму по заказам со статусом "оплачено".

### REST API

API доступно по префиксу `/api/` 
1. #### Добавление заказа
- Метод: `POST`

- URL: `/api/orders/`

- Параметры (JSON):
  
`table_number` (int, обязательный) — номер стола.

`items` (JSON, обязательный) — список блюд с ценами, например:` [{"name": "Салат", "price": 5.99}]`.

Пример запроса:
```
{
  "table_number": 3,
  "items": [{"name": "Суп", "price": 7.50}, {"name": "Кофе", "price": 2.30}]
}
```
Пример ответа:
```
{
  "id": 1,
  "table_number": 3,
  "items": [{"name": "Суп", "price": 7.50}, {"name": "Кофе", "price": 2.30}],
  "total_price": 9.80,
  "status": "waiting"
}
```

2. #### Удаление заказа

- Метод: `DELETE`

- URL: `/api/orders/<id>/` (где `<id>` — идентификатор заказа).

Пример запроса:

`DELETE http://localhost:8000/api/orders/1/`


3. #### Поиск и отображение заказов

- Метод: `GET`

- URL: `/api/orders/?table_number=<number>&status=<status>`

- Параметры (опционально):

`table_number` (int) — номер стола.

`status` (string) — статус заказа ("waiting", "ready", "paid").

Пример запроса:
```
GET http://localhost:8000/api/orders/?status=paid
```

4. #### Изменение статуса заказа
- Метод: `PATCH` или `PUT`

- URL: `/api/orders/<id>/`

Параметры (JSON): Обновляемые поля, например:

```
{
  "status": "paid"
}
```

5. #### Расчет выручки
   
- Метод: `GET`

- URL: `/api/revenue/`

Пример ответа:

```
{
  "revenue": "123.45"
}
```

6. #### Получение меню
 
- Метод: GET

- URL: ```/api/menu/```

Пример ответа:
```
[
  {
    "id": 1,
    "name": "Суп дня",
    "price": 4.50,
    "category": "Основное",
    "description": "Легкий овощной суп"
  },
  {
    "id": 2,
    "name": "Кофе",
    "price": 2.00,
    "category": "Напитки",
    "description": ""
  }
]
```

## Структура проекта 📂

### Корневая директория
- `cafe_orders/` — Основная конфигурация Django.
     - `settings.py` — Настройки проекта (база данных, middleware, приложения).
     - `urls.py` — Глобальные маршруты.
     - `wsgi.py` — Конфигурация для развертывания.

### Директория `orders/`

- `admin.py` — Регистрация моделей в админ-панели Django.
- `apps.py` — Конфигурация приложения.
- `forms.py` — Формы для веб-интерфейса.
- `models.py` — Модели данных (например, модель Order).
- `urls.py` — Локальные маршруты приложения.
- `views.py` — Логика представлений (веб-интерфейс и API).
- `migrations/` — Миграции базы данных.
- `templates/` — HTML-шаблоны:
     - `base.html` — Базовый шаблон.
     - `orders/` — Шаблоны для заказов (например, order_list.html, order_form.html).
- `static/` — Статические файлы:
     - `css/stile.css` — Стили для интерфейса.

### Дополнительно
- requirements.txt — Список зависимостей (Django, Django REST Framework и др.).
- manage.py — Утилита для управления проектом.
- README.md — Документация.

## Стек технологий 
- Python 3.8+.

- Django 4+ (включая Django ORM).

- Django REST Framework (для API).

- HTML/CSS (для веб-интерфейса).

- SQLite/PostgreSQL (для хранения данных).


