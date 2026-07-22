from .base import BaseParser

class NewsParser(BaseParser):
    """Парсер новостных сайтов — заголовки, даты, ссылки"""

    def parse(self, url, limit=50):
        html = self.fetch(url)
        soup = self.soup(html)
        items = []

        # универсальные селекторы — подходят для многих новостников
        articles = soup.select("article, .news-item, .post, .article")[:limit]

        for art in articles:
            title_el = art.select_one("h1, h2, h3, .title, .headline")
            link_el = art.select_one("a[href]")
            date_el = art.select_one("time, .date, .published")

            if not title_el:
                continue

            items.append({
                "title": title_el.get_text(strip=True),
                "link": link_el.get("href", "") if link_el else "",
                "date": date_el.get_text(strip=True) if date_el else "",
                "source": url,
            })

        return items
