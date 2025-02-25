# -*- coding: utf-8 -*-

import os,sys

#путь к проекту
sys.path.append('/home/m/mkeytop/public_html/mkey/public_html')
#путь к фреймворку
sys.path.append('/home/m/mkeytop/public_html/mkey')
#путь к виртуальному окружению
sys.path.append('/home/m/mkeytop/.djangovenv/lib/python3.8/site-packages/')
#исключить системную директорию

os.environ["DJANGO_SETTINGS_MODULE"] = "grigorevs.settings"

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()