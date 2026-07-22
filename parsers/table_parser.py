from .base import BaseParser

class TableParser(BaseParser):
    """Парсит HTML-таблицы в список словарей"""

    def parse(self, url, limit=50):
        html = self.fetch(url)
        soup = self.soup(html)

        table = soup.find("table")
        if not table:
            return []

        # заголовки
        headers = []
        header_row = table.find("tr")
        if header_row:
            headers = [th.get_text(strip=True) for th in header_row.find_all(["th", "td"])]

        rows = []
        for tr in table.find_all("tr")[1:limit + 1]:
            cells = [td.get_text(strip=True) for td in tr.find_all(["td", "th"])]
            if not cells:
                continue
            if headers and len(headers) == len(cells):
                rows.append(dict(zip(headers, cells)))
            else:
                # если заголовки не совпали — используем индексы
                rows.append({f"col_{i}": cell for i, cell in enumerate(cells)})

        return rows
