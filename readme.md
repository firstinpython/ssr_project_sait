## Структура проекта
[Общая структура](#общая-структура)\
[Система управления парком автомобилей](#система-управления-парком-автомобилей)\
[Система оплаты услуг](#система-оплаты-услуг)\
[Автомобиль](#автомобиль)\
[Мобильное приложение клиента](#мобильное-приложение-клиента)

### Общая структура

project/
│── module/ **Название модуля** \
│ │── config/ **Содержит файл с зависимостями которые используются в проекте**\
│ └── requirements.txt\
│ │── data/ **Данные используемые в модуле, наличие по необходимости (может быть instance, в случае использования БД)** \
│ │ └── data.json\
│ │── src/ **Основной код модуля**\
│ │ ├── \_\_init\_\_.py **Инициализация приложения (стандартный для всех модулей)** \
│ │ └── main.py **Код приложения** \
│ │── Dockerfile **Сборка образа (стандартный для всех модулей, по необходимости вносяться изменения)** \
└─── start.py **Запуск модуля**

Перед запуском настроить среду для разработки:

```make dev_install```

Пример запуска:

```python3 module/start.py```

Важно! При локальном запуске (не в Docker образе) заменить URL на localhost и так же порт

Пример:

```MANAGMENT_URL = 'http://management_system:8000'``` на ```MANAGMENT_URL = 'http://0.0.0.0:8001'```

### Система управления парком автомобилей

#### cars

Программный имитатор управления парком автомобилей, содержит простую базу данных для хранения данных клиента

### API

#### URL http://0.0.0.0:8003

|Название метода|Тип запроса|Входные параметры|Ответ (успешный)|Описание|
|:--|:--|:--|:--|:--|
|/cars|GET||list[string]|Опрашивает доступные автомобили и отдаёт список свободных автомобилей|
|/tariff|GET||list[string]|Отдает список тарифов|
|/telemetry/<string:brand>|POST|Имя автомобиля||Функция для получения телеметрии от автомобилей во время поездки|
|/access/<string:name>|POST|Имя клиента|{'access': bool, 'tariff': string, 'car': string}| Проверка доступа клиента до автомобиля|
|/confirm_prepayment/<string:name>|POST|Имя клиента||Фукнция получения потверждений об оплате предоплаты клиента от системы оплаты услуг|
|/confirm_payment/<string:name>|POST|Имя клиента|{'car': string, 'name': string, 'final_amount': int,'created_at': time, 'elapsed_time': int, 'tarif': string}|Фукнция получения потверждений об оплате поездки клиента от системы оплаты услуг, формирует финальный чек о поездке и передаёт клиенту|
|/select/car/<string:brand>|POST|{'client_name': string, 'experience': int, 'tariff': string}|{'id': int, 'amount': int, 'client_id': int, 'status': string}|Бронирование и рассчет предоплаты в зависимости от функций автомобиля|
|/return/<string:name>|POST|Имя клиента|{'id': int, 'amount': int, 'status': string, 'client_id': int}|Рассчёт стоимости всей поездки в зависимости от опыта и тарифа, создание оплаты. Получает запрос от автомобиля|

|Название|Тип|
|:--|:--|
|/get|{'string':''}|
### Система оплаты услуг

#### payment-system

Программный имитатор банковской системы, содержит базу данных для сохранения операций клиента

### API

#### URL http://127.0.0.1:8000/api/v1
### Users

| Название метода                            | Тип запроса | Входные параметры                                                                                                                                 | Ответ (успешный)                                                                                                                                                                                                                                                                                                                                                                                 |Описание|
|:-------------------------------------------|:------------|:--------------------------------------------------------------------------------------------------------------------------------------------------|:-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|:--|
| /users/                                    | GET         | str                                                                                                                                               | {'id': int, 'name': string}                                                                                                                                                                                                                                                                                                                                                                      |Создает или отдаёт клиента если он существует в базе системы оплаты услуг|
| /create_user/                              | POST        | {"username":str,"first_name":str,"last_name":str,"email":str,"age":int,"role":int,"profession_category":int,"dev_stack":list[int],"password":str} | status 200                                                                                                                                                                                                                                                                                                                                                                                       |Получение по ИД (системы оплаты услуг) клиента|
| /profile/                                  | GET         | str                                                                                                                                               | {"user_profile": {"username": str,"first_name": str,"last_name": str,"email": str,"age": int,"role": {"name_role": str},"profession_category": {"name_prof_category": str},"dev_stack": [{"user_stack": str}]},"projects": [{"name_project": str,"status": {"name_status": str,}}]}                                                                                                              |Получение всех неоплаченных счётов клиента|



### Projects

| Название метода                     | Тип запроса | Входные параметры |Ответ (успешный)|Описание|
|:------------------------------------|:------------|:------------------|:--|:--|
| /create_project/                    | POST        | str               |[{"brand": string,"is_running": bool,"speed": int,"coordinates": (int, int), "occupied_by": string, "trip_time": int, "has_air_conditioner": bool, "has_heater": bool, "has_navigator": bool, "tariff ": string}]|Возвращает все статусы автомобилей|
| /<int:project_id>/addproject/       | POST        | Имя автомобиля    |string|Запуск автомобиля|
| /list_projects/                     | GET         | Имя автомобиля    |string|Остановка автомобиля|
| /<str:project_slug>/update_project/ | PUT         | Имя автомобиля    |{"brand": string,"is_running": bool,"speed": int,"coordinates": (int, int), "occupied_by": string, "trip_time": int, "has_air_conditioner": bool, "has_heater": bool, "has_navigator": bool, "tariff ": string}|Получени статуса автомобиля|
| /<int:project_id>/delete/           | DELETE      | Имя клиента       |string|Арендовать автомобиль|



### Tasks

|Название метода|Тип запроса|Входные параметры|Ответ (успешный)|Описание|
|:--|:--|:--|:--|:--|
|/cars|POST|{"name": string, "experience": int}|{'id': int, 'amount': int, 'client_id': int, 'status': string}|Выбор автомобиля из свободных, выбор тарифа и получение счёта для оплаты предоплаты|
|/start_drive|POST|{name: string}|string|Начало поездки, проверка доступа до автомобиля|
|/stop_drive|POST|{name: string}|{'id': int, 'amount': int, 'status': string, 'client_id': int}|Окончание поездки, возвращение автомобиля. Так же присылается итоговая оплата поездки в зависимости от тарифа|
|/prepayment|POST|{'id': int, 'amount': int, 'client_id': int, 'status': string}|{'invoice_id': int}|Оплата предоплаты|
|/final_pay|POST|{'invoice_id': int}|{'car': string, 'name': string, 'final_amount': int,'created_at': time, 'elapsed_time': int, 'tarif': string}|Оплата поездки и получение финального чека|


### Comments

|Название метода|Тип запроса|Входные параметры|Ответ (успешный)|Описание|
|:--|:--|:--|:--|:--|
|/cars|POST|{"name": string, "experience": int}|{'id': int, 'amount': int, 'client_id': int, 'status': string}|Выбор автомобиля из свободных, выбор тарифа и получение счёта для оплаты предоплаты|
|/start_drive|POST|{name: string}|string|Начало поездки, проверка доступа до автомобиля|
|/stop_drive|POST|{name: string}|{'id': int, 'amount': int, 'status': string, 'client_id': int}|Окончание поездки, возвращение автомобиля. Так же присылается итоговая оплата поездки в зависимости от тарифа|
|/prepayment|POST|{'id': int, 'amount': int, 'client_id': int, 'status': string}|{'invoice_id': int}|Оплата предоплаты|
|/final_pay|POST|{'invoice_id': int}|{'car': string, 'name': string, 'final_amount': int,'created_at': time, 'elapsed_time': int, 'tarif': string}|Оплата поездки и получение финального чека|
