# Сайт для сокращения ссылок - YaCut
## Оглавление
1. [Описание](https://github.com/TomatoInOil/yacut#описание)
2. [Используемые технологии](https://github.com/TomatoInOil/yacut#используемые-технологии)
3. [Как развернуть проект?](https://github.com/TomatoInOil/yacut#как-развернуть-проект)
4. [Примеры запросов API](https://github.com/TomatoInOil/yacut#примеры-запросов-api)
5. [Автор](https://github.com/TomatoInOil/yacut#автор)
## Описание
На главной странице сайта есть форма для сокращения ссылки, можно задать свой вариант сокращения ссылки. Также в проекте описан API интерфейс.
## Используемые технологии
- `Python`
- `Flask`
- `wtforms`
- `SQLAlchemy`
## Как развернуть проект?
Склонировать репозиторий 
```BASH
git clone https://github.com/TomatoInOil/yacut.git
```
Перейти в корневую папку проекта
```BASH
cd yacut/
```
Создать виртуальное окружение
```BASH
python -m venv venv
```
Активировать виртуальное окружение
```BASH
source venv/Scripts/activate
```
Установить зависимости
```BASH
pip install -r requirements.txt
```
Заполнить `.env` по образцу `example.env`  
Запустить приложение
```BASH
Flask run
```
## Примеры запросов API
.../api/id/{short_id}/  
Получение оригинальной ссылки по id короткой  
Пример ответа (200)
```JSON
{
  "url": "https://string.sting/"
}
```
.../api/id/  
Сокращение ссылки  
Пример запроса  
```JSON
{
  "url": "https://string.sting/very_long_string/",
  "custom_id": "string"
}
```
Пример ответа (201)  
```JSON
{
  "url": "https://string.sting/very_long_string/",
  "short_link": "https://host/string/"
}
```
## Автор
Проект выполнен в рамках обучения в Яндекс.Практикум [Даниилом Паутовым](https://github.com/TomatoInOil)
