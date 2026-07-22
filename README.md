# Web Scraper

Универсальный парсер данных с сайтов. Три режима: новости, товары, таблицы. Экспорт в CSV/JSON/Excel.

## Установка

```bash
pip install -r requirements.txt
```

## Использование

```bash
# новости
python scraper.py news https://example.com/news -o news -f csv --limit 30

# товары
python scraper.py products https://shop.example.com/catalog -o products -f xlsx

# таблица
python scraper.py table https://site.com/rates -o rates -f json
```

## Параметры

| Параметр | Описание |
|----------|----------|
| `mode` | news, products или table |
| `url` | URL страницы |
| `-o` | имя файла без расширения (default: output) |
| `-f` | формат: csv, json, xlsx (default: csv) |
| `--limit` | макс. записей (default: 50) |
| `--delay` | пауза между запросами в секундах (default: 1.0) |

## Структура

```
scraper.py           — CLI точка входа
parsers/
  base.py            — базовый класс с fetch/soup
  news_parser.py     — новости
  product_parser.py  — товары
  table_parser.py    — таблицы
utils/
  export.py          — экспорт в csv/json/xlsx
  proxy.py           — ротация прокси (заготовка)
config.yaml          — настройки
```

## Важно

- Парсер делает ротацию User-Agent, но если сайт банит по IP — добавь прокси в config.yaml
- Не ставь delay меньше 1 секунды, это невежливо
- Для xlsx нужен openpyxl (он в requirements)

Если нужен парсер под конкретный сайт — пиши, сделаю.
