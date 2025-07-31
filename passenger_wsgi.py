import os
import sys

# 1) Add project root and project package to PYTHONPATH
project_root = os.path.dirname(__file__)
sys.path.insert(0, project_root)
sys.path.insert(0, os.path.join(project_root, "blackstone"))

# 2) Set the settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "blackstone.settings")

# 3) Get the WSGI app
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
