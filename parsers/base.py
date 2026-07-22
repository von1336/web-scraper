import time
import random
import requests
from bs4 import BeautifulSoup

# ротируем User-Agent чтобы не забанили сразу
USER_AGENTS = [
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
]

class BaseParser:
    def __init__(self, config=None, delay=1.0):
        self.config = config or {}
        self.delay = delay
        self.session = requests.Session()

    def fetch(self, url):
        """Скачивает страницу с ротацией UA и паузой"""
        headers = {"User-Agent": random.choice(USER_AGENTS)}
        time.sleep(self.delay + random.uniform(0, 0.5))  # небольшой рандом чтобы не палиться
        resp = self.session.get(url, headers=headers, timeout=15)
        resp.raise_for_status()
        return resp.text

    def soup(self, html):
        return BeautifulSoup(html, "lxml")

    def parse(self, url, limit=50):
        raise NotImplementedError
