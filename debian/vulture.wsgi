import os, sys
sys.path.append('/var/www/vulture')
sys.path.append('/var/www/vulture/admin')
sys.path.append("/opt/vulture/lib/Python/modules")
os.environ['DJANGO_SETTINGS_MODULE'] = 'admin.settings'

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
