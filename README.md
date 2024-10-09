# Тестовое задание IT-Solutions

Веб-приложение для управления информацией об автомобилях с использованием API


## Запуск проекта:

1) Клонируйте репозиторий с проектом

```bash
git clone https://github.com/Egore000/Test-task.git 
cd Test-task/
```

2) Запустите `docker-compose`

```bash
docker compose up
```

3) Примените миграции

```bash
docker compose run django python manage.py migrate
```

4) Создайте суперпользователя
   
```bash
docker compose run django python manage.py createsuperuser
```

## Использование приложения

* Регистрация пользователя:
  1) С помощью админ-панели: http://127.0.0.1:8000/admin/
   
    <img src="docs/images/admin.png" width=800px alt="admin">
   
  2) Через форму создания пользователя: http://127.0.0.1:8000/account/register/
   
   <img src="docs/images/registration.png" width=800px alt="registation">
  
* Список всех авто: http://127.0.0.1:8000/cars/

    <img src="docs/images/homepage.png" width=800px alt="cars">

* Список автомобилей пользователя: http://127.0.0.1:8000/cars/my/

    <img src="docs/images/my_cars.png" width=800px alt="my">

* Информация о конкретном автомобиле: http://127.0.0.1:8000/cars/{car_id}/

    <img src="docs/images/detail.png" width=800px alt="detail">

## API

Документация к API в формате Swagger и Redoc доступна по адресам:

Swagger: http://127.0.0.1:8000/api/docs/

<img src="docs/images/swagger.png" width=800px alt="swagger">

Redoc: http://127.0.0.1:8000/api/redoc/

<img src="docs/images/redoc.png" width=800px alt="redoc">

