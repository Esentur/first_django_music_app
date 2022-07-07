# 1) ##########################################################

# python3 -m venv venv - создаем виртуальное окружение
# source venv/bin/activate - активация виртуального окружения
# pip freeze список установленных библиотек
# deactivate - выйти из виртуального окружения

# 2) ###########################################################

# touch requirements.txt - создаем requirements.txt
    # django
    # djangorestframework

#pip install -r requirements.txt

# 3) ############################################################

# django-admin startproject name_project . - создаем главное приложение нашего проекта

##### Есть 2 варианта создаения определенного приложения ###########

# django-admin startapp name_app - создаем определенное приложение

# ./manage.py startapp name_app - создаем определенное приложение

# in main_app - settings.py - installed app - добавить 'name_app',
# in name_app - models.py - создаем свои классы т.е таблицы в бд
# in name_app - admin.py - импортируем классы и прописываем регистрыf
# ./manage.py runserver

# ./manage.py makemigrations - создает миграцию
# ./manage.py migrate - применяет ее
# ./manage.py createsuperuser - создает супер пользователя

# ./manage.py runserver
# ./manage.py makemigrations music_app
# ./manage.py migrate