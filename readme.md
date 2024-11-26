# API
Установка и запуск проекта
1. Клонирование репозитория
Сначала склонируйте репозиторий на свой локальный компьютер:

bash
Copy
git clone https://github.com/yourusername/task-management-system.git
cd task-management-system
2. Создание виртуального окружения
Создайте и активируйте виртуальное окружение:

bash
Copy
python3 -m venv venv
source venv/bin/activate  # Для Linux/MacOS
# или
venv\Scripts\activate  # Для Windows
3. Установка зависимостей
Установите необходимые зависимости:

bash
Copy
pip install -r requirements.txt
4. Настройка базы данных
Создайте и примените миграции:

bash
Copy
python manage.py makemigrations
python manage.py migrate
5. Создание суперпользователя
Создайте суперпользователя для доступа к административной панели:

bash
Copy
python manage.py createsuperuser
6. Запуск сервера
Запустите сервер разработки Django:

bash
Copy
python manage.py runserver
Теперь вы можете открыть браузер и перейти по адресу http://127.0.0.1:8000/ для доступа к приложению.

Доступные URL-адреса
Swagger и Redoc
Swagger JSON: http://127.0.0.1:8000/swagger.json/

Swagger UI: http://127.0.0.1:8000/swagger/

Redoc UI: http://127.0.0.1:8000/redoc/

# Пользователи
Список пользователей: http://127.0.0.1:8000/users/

Создание пользователя: http://127.0.0.1:8000/create_user/

Профиль пользователя: http://127.0.0.1:8000/user_profile/

# Проекты
Создание проекта: http://127.0.0.1:8000/create_project/

Добавление пользователей в проект: http://127.0.0.1:8000/<int:project_id>/addproject/

Список проектов: http://127.0.0.1:8000/list_projects/

Обновление проекта: http://127.0.0.1:8000/<str:project_slug>/update_project

Удаление проекта: http://127.0.0.1:8000/<int:project_id>/delete

# Задачи
Создание задачи: http://127.0.0.1:8000/<int:project_id>/create_task/

Список задач: http://127.0.0.1:8000/<int:project_id>/list_tasks/

Удаление задачи: http://127.0.0.1:8000/<int:project_id>/<int:task_id>/delete/

Обновление задачи: http://127.0.0.1:8000/<str:project_slug>/<str:task_slug>/update_task/

Обновление комментария: http://127.0.0.1:8000/<str:project_slug>/<str:task_slug>/<str:comment_slug>/

# Комментарии
Создание комментария: http://127.0.0.1:8000/<int:project_id>/create_comment

Список комментариев: http://127.0.0.1:8000/<int:project_id>/<int:task_id>/lists_comments/

Удаление комментария: http://127.0.0.1:8000/<str:project_slug>/<str:task_slug>/<str:comment_slug>/delete_comment/

# JWT-токены
Получение токена: http://127.0.0.1:8000/api/token/

Обновление токена: http://127.0.0.1:8000/api/token/refresh/

Проверка токена: http://127.0.0.1:8000/api/token/verify/

# Тестирование
Для запуска тестов используйте следующую команду:

bash
Copy
python manage.py test
