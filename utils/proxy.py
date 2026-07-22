import random
import time

# если парсишь много — тут можно добавить прокси
# пока просто заготовка

class ProxyRotator:
    def __init__(self, proxies=None):
        self.proxies = proxies or []
        self._idx = 0

    def get(self):
        if not self.proxies:
            return None
        self._idx = (self._idx + 1) % len(self.proxies)
        return self.proxies[self._idx]

    def random_proxy(self):
        return random.choice(self.proxies) if self.proxies else None
