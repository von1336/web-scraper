import argparse
import logging
import sys
from pathlib import Path
import yaml

from parsers.news_parser import NewsParser
from parsers.product_parser import ProductParser
from parsers.table_parser import TableParser
from utils.export import Exporter

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] %(message)s'
)
log = logging.getLogger(__name__)

def load_config():
    cfg_path = Path(__file__).parent / "config.yaml"
    if cfg_path.exists():
        with open(cfg_path, encoding="utf-8") as f:
            return yaml.safe_load(f)
    return {}

def main():
    parser = argparse.ArgumentParser(description="Универсальный парсер данных с сайтов")
    parser.add_argument("mode", choices=["news", "products", "table"], help="Что парсим")
    parser.add_argument("url", help="URL страницы")
    parser.add_argument("-o", "--output", default="output", help="Имя файла без расширения")
    parser.add_argument("-f", "--format", choices=["csv", "json", "xlsx"], default="csv")
    parser.add_argument("--limit", type=int, default=50, help="Макс. количество записей")
    parser.add_argument("--delay", type=float, default=1.0, help="Пауза между запросами, сек")
    args = parser.parse_args()

    config = load_config()

    # выбираем парсер
    parsers = {
        "news": NewsParser,
        "products": ProductParser,
        "table": TableParser,
    }
    ParserCls = parsers[args.mode]

    log.info(f"Запуск парсера '{args.mode}' для {args.url}")
    p = ParserCls(config=config, delay=args.delay)

    try:
        data = p.parse(args.url, limit=args.limit)
    except Exception as e:
        log.error(f"Ошибка парсинга: {e}")
        sys.exit(1)

    if not data:
        log.warning("Ничего не спарсилось. Проверь селекторы или URL.")
        sys.exit(0)

    log.info(f"Спарсено {len(data)} записей")

    exporter = Exporter()
    out_file = exporter.save(data, args.output, args.format)
    log.info(f"Сохранено в {out_file}")

if __name__ == "__main__":
    main()
