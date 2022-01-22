#WSGI file is required for a flask application to run in production
#!/usr/bin/python
import sys
sys.path.insert(0,"/var/www/html/flaskapp")

from flaskapp import app as application