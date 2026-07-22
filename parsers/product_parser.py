import re
from .base import BaseParser

class ProductParser(BaseParser):
    """Парсер карточек товаров — название, цена, наличие"""

    def parse(self, url, limit=50):
        html = self.fetch(url)
        soup = self.soup(html)
        items = []

        # ищем типичные блоки товаров
        cards = soup.select(".product, .item, .card, [data-product]")[:limit]

        for card in cards:
            name_el = card.select_one(".product-name, .item-title, .name, h2, h3")
            price_el = card.select_one(".price, .cost, [class*=price]")

            if not name_el:
                continue

            price_raw = price_el.get_text(strip=True) if price_el else ""
            # вытаскиваем цифры из цены
            price_num = re.sub(r"[^\d]", "", price_raw)

            items.append({
                "name": name_el.get_text(strip=True),
                "price_raw": price_raw,
                "price": int(price_num) if price_num else None,
                "url": url,
            })

        return items
