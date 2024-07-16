1. Склонируйте репозиторий с помощью команды git clone:
<br><br/>
git clone https://github.com/lakeroko/Project
<br><br/>
2. Создайте виртуальное окружение Python, если это необходимо:
<br><br/>
python -m venv venv
<br><br/>
3. Активируйте виртуальное окружение. Для Windows:
<br><br/>
venv\Scripts\activate
<br><br/>
Для macOS и Linux:
<br><br/>
source venv/bin/activate
<br><br/>
4. Установите зависимости проекта:
<br><br/>
pip install -r installed_libraries.txt
<br><br/>
5. Выполните миграции базы данных с помощью команды:
<br><br/>
python manage.py makemigrations
python manage.py migrate
<br><br/>
6. Создайте суперпользователя:
<br><br/>
python manage.py createsuperuser