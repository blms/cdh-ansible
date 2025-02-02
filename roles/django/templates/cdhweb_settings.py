{% extends "local_settings.py" %}
"""
Django local settings for cdhweb
"""

{% block extra_config %}
NEVERCACHE_KEY = "{{ nevercache_key }}"

# set compress offline for django-compressor
COMPRESS_OFFLINE = True

# Media root settings for production
MEDIA_ROOT = '{{ media_root }}'
MEDIA_URL = '/media/'
STATIC_URL = "/static/"

# Allow SVG
FILEBROWSER_ESCAPED_EXTENSIONS = []

# managers for broken email 404s
MANAGERS = [('CDH Dev Team', 'cdhdevteam@princeton.edu'),]
# ignore php, asp, aspx, jsp, jspa, with or without trailing slash
import re
IGNORABLE_404_URLS = [re.compile('\.(php|aspx?|jspa?)(\/$|$)')]


{% if qa is not defined %}
# Turn on Google Analytics
INCLUDE_ANALYTICS = True
GTAGS_ANALYTICS_ID = 'G-864528T1N5'
{% endif %}

{% endblock %}
