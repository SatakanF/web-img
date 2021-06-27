command = '/home/adminuks/web-application/env/bin/gunicorn'
pythonpath = '/home/adminuks/web-application/ImageSearch/'
bind = '127.0.0.1:8001'
workers = 3
user = 'adminuks'
limit_request_fields = 32000
limit_request_field_size = 0
raw_env = 'DJANGO_SETTINGS_MODULE=project.settings'