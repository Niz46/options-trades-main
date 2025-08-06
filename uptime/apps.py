# uptime/apps.py
import threading
import time
import requests
from django.apps import AppConfig
from django.conf import settings

class UptimeConfig(AppConfig):
    name = "uptime"

    def ready(self):
        # Only spawn one thread, and only when runserver or WSGI starts
        def self_ping():
            url = getattr(settings, "SELF_PING_URL", None)
            if not url:
                return

            # Wait a bit to let everything boot (migrations, DB pools, etc)
            time.sleep(60)

            while True:
                try:
                    requests.get(url, timeout=5)
                except Exception:
                    # ignore any errors (network, DNS, etc)
                    pass
                # ping every 7 minutes
                time.sleep(420)

        thread = threading.Thread(target=self_ping, daemon=True)
        thread.start()
