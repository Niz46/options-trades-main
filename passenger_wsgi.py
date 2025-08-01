import os
import sys
import logging

# Log to stderr so Passenger/Apache captures it
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

# 1) Add your project’s root to the Python path
project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, "blackstone"))

# 2) Set the Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackstone.settings")

try:
    # 3) Initialize Django
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()
except Exception:
    logging.exception("Failed to load WSGI application")
    # Re-raise so Passenger still sees a 500
    raise
