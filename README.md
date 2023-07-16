### Бот для отправки уведомлений с обратной свсязью (MVP)
Бот отправляет запросы согласно указаных в Google sheet данных.

## Как установить

Для написания скрипта использовался __Python 3.11__.

1. Склонировать репозиторий.
   
2. Создать виртуальное окружение.
    ```bash
    python -m venv env
    ```
    ```bash
    . env/bin/activate
    ```
3. Установить зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Создать `.env`:
   ```bash
   touch .env
   ```
5. Занесите в `.env` необходимые параметры:

   - `TELEGRAM_BOT_TOKEN` - токен Телеграм-бота. Как получить, можно посмотреть [тут](https://way23.ru/регистрация-бота-в-telegram.html).
   - `MANAGER_TG_ID` - ID Telegram менеджера, сюда будут приходить уведомления об ответах сотрудников.

## Как запустить

Для запуска бота:
```bash
python main.py
```

## Тестовая версия

Бот: [Test_bot](https://t.me/Space_poster_bot)

Google sheet: [Notifications](https://docs.google.com/spreadsheets/d/1IviENacVBm9xCiWSH7M4-E_368x7WnTVIanTLNmN-QA/edit?usp=sharing)

Сервер запущен на прерываемой ВМ (Yandex.cloud). Если не работает, пишите в Телеграм ([Роман Окатьев](https://t.me/RomanOkatev)), оперативно запущу.



