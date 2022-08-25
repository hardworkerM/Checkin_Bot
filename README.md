# Checkin_Bot
Хакатон от Школа21 Сбера.
**Задача** "Необходимо разработать Telegram-бота для чекина на школьных мероприятиях."
Команда:

## Оглавление

1. [Описание задачи](#описание-задачи)
2. [Архитектура проекта](#архитектура-проекта)
3. [Результаты](#результаты)
____

## Описание задачи
Полное описание задачи вы можете посмотреть [здесь.](https://github.com/hardworkerM/Checkin_Bot/blob/main/Checkin_bot_task.pdf) 

**Команда:**
[urycherd](https://github.com/urycherd) [mikabuto](https://github.com/mikabuto) и другие

[:arrow_up:Оглавление](#оглавление)
____
## Архитектура проекта
- /data - хранение генерируемых файлов отчётности и qr-кодов
- [/database](https://github.com/hardworkerM/Checkin_Bot/tree/main/database) - подключение базы данных и функции sql запросов
- [/deeplink](https://github.com/hardworkerM/Checkin_Bot/tree/main/deeplink) - Генерация qr-кода мероприятия
- [/handlers](https://github.com/hardworkerM/Checkin_Bot/tree/main/handlers) - хендлеры для взаимодействия бота с пользователем
- [/keyboards](https://github.com/hardworkerM/Checkin_Bot/tree/main/keyboards) - функции создания Inline и Reply клавиатур
- [/state](https://github.com/hardworkerM/Checkin_Bot/tree/main/state) - класс состояний
- [/utils](https://github.com/hardworkerM/Checkin_Bot/tree/main/utils) - вспомогательные, форматирующие функции
- app.py и create_bot.py - подключение и активизация бота.

[:arrow_up:Оглавление](#оглавление)
____
## Результаты
Функционал бота [ютуб](https://youtu.be/U5yTr65kLro)

[:arrow_up:Оглавление](#оглавление)
____
