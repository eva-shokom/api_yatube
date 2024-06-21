# Проект API для Yatube

Добро пожаловать в наш проект **API для Yatube**! Yatube - это социальная сеть для публикации личных дневников. Здесь пользователь может создать свою страницу и публиковать на ней посты. Для каждого поста нужно указать категорию, а также опционально локацию. Чужие посты также можно читать и комментировать.

В нашем проекте вы сможете:
- получить список всех публикаций, а также любую отдельную публикацию и комментарии к ней *(даже если вы анонимный пользователь!)*
- добавить, редактировать и удалить собственную публикацию
- комментировать свои и чужие публикации *(доступно только авторизованным пользвателям!)*, редактировать и удалять собственные комментарии
- посмотреть, какие у нас есть сообщества, а также изучить информацию о каждом сообществе
- подписаться на других пользователей и посмотреть свои подписки

## Стек технологий

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)
![Postman](https://img.shields.io/badge/Postman-FF6C37?style=for-the-badge&logo=postman&logoColor=white)

## Как запустить проект

Для установки проекта необходимо выполнить следующие шаги:

1. Склонировать репозиторий.

```bash
git clone git@github.com:eva-shokom/api_yatube.git
```

2. Находясь в корневой директории проекта, создать виртуальное окружение и активировать его

```bash
python -m venv venv
```

Для Windows:
```bash
source venv/Scripts/activate
```

Для Linux/Mac:
```bash
source venv/bin/activate
```

3. Обновить pip, установить необходимые зависимости

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

4. Перейти в папку yatube_api
  
```bash
cd yatube_api
```

5. Выполнить миграции и заполнить базу данных из файлов csv

```bash
python manage.py migrate
```

6. Запустить сервер

```bash
python manage.py runserver
```

После выполнения этих шагов проект будет запущен и станет доступен по адресу [localhost:8000/api/v1/](http://localhost:8000/api/v1/)

Когда вы запустите проект, по этой [ссылке](http://127.0.0.1:8000/redoc/) будет доступна документация для API Yatube. В документации описано, как должен работать ваш API. Там же вы сможете посмотреть алгоритм аутентификации пользователей с помощью JWT-токена и найдете примеры запросов к API. *Документация представлена в формате Redoc*.

#### Надеемся, вам у нас понравится!

---

Проект подготовила [eva-shokom](https://github.com/eva-shokom/).
Если у вас возникнут вопросы, пожелания и предложения, вы можете обращаться к авторам этого проекта. Будем рады видеть вашу обратную связь! 
