import sys
import os

# 1. Add your project’s root directory to the Python path
project_home = os.path.dirname(__file__)
if project_home not in sys.path:
    sys.path.insert(0, project_home)

# 2. Set Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackstone.settings")

# 3. Activate your virtualenv, if not auto‑activated by cPanel
#    passenger_wsgi will do this for you if you use the “Setup Python App” tool.

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()