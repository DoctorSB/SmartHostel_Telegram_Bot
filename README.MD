## **Телеграмм бот**

Этот телеграмм бот создан для упрощения и автоматизации жизни жителей хостела

## **Инструкции по использованию**

Найдите бота в телеграмме (@smart_hostel_bot).
Начните чат с ботом, нажав на кнопку "Старт".
Следуйте инструкциям, которые предоставит бот.
Команды бота

**/start** - начать работу с ботом.

## **Как запустить бота**

Клонируйте репозиторий:

**git clone https://github.com/DoctorSB/SmartHostel_Telegram_Bot**

Установите зависимости, выполнив следующую команду в терминале:
```
python3 -m venv venv

.\venv\Scripts\activate

pip install -r requirements.txt
```

Создайте файл **.env** и запишите в него следующие данные и замените их на свои:
```
BOT_CONTAINER_NAME=bot_container_name
BOT_IMAGE_NAME=botimage_name
BOT_NAME=BOT_NAME
BOT_TOKEN=TOKEN
ADMINS=
USE_REDIS=False

DB_USER=exampleDBUserName
PG_PASSWORD=examplePostgresPass
DB_PASS=exampleDBPassword
DB_NAME=exampleDBName
DB_HOST=127.0.0.1
```

Запустите бота:

**python3 bot.py**
