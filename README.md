# MMO_D16.7
SkillFactory homeworck
Согласно ТЗ по заданю был создан проект сайта по популярной MMORPG игре на котором можно размещать различные записи и оставлять на них реакции.

Запуск проекта:
Т.к. данный проект разрабатывался на Windows 11, все нижеуказанные команды приведены для запуска проекта на такой же ОС.

1. Открываем проект с помощью IDE (PyCharm, Visual Studio Code, и т.п.)


2. Открываем окно терминала и переходим в директорию проекта:

cd MMOBoard


3. Создаём виртуальное окружение для проекта:

py -m venv venv


4. Активируем виртуальное окружение:

venv\scripts\activate


5. Переходим в директорию MMOBoard:

cd MMOBoard


6. Устанавливаем необходимые для работы проекта зависимости (на это уйдёт какое-то время, поэтому нужно будет немного подождать):

pip install -r requirements.txt


7. Открываем 2 дополнительных окна терминала (т.е. всего их должно быть открыто три). В каждом из них переходим в директорию проекта и активируем виртуальное окружение:

cd MMOBoard

venv\scripts\activate


8. В первом окне терминала запускаем Django-сервер:

py manage.py runserver


9. Во втором окне терминала переходим в директорию config и запускаем Celery для асинхронной обработки задач по отправке писем (все письма должны приходить в текстовом формате именно в это окно терминала):

cd MMOBoard

celery -A MMOBoard worker -l info -P threads --pool=solo


10. В третьем окне терминала переходим в директорию config и запускаем обработку периодических задач через Celery (очистка неподтверждённых аккаунтов пользователей и удаление неиспользованных кодов авторизации из БД):

cd MMOBoard

celery -A MMOBoard beat -l info


11. Переходим по ссылке:

http://127.0.0.1:8000/board/

Дальнейшее использование сайта должно быть интуитивно понятным.
