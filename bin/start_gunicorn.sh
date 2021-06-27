#!/bin/bash
	source /home/adminuks/web-application/env/bin/activate
	source /home/adminuks/web-application/env/bin/postactivate
	exec gunicorn  -c "/home/adminuks/web-application/ImageSearch/config/gunicorn_conf.py" ImageSearch.wsgi