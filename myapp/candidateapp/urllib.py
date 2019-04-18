import os
from urllib.parse import urlparse
# from urlparse import urlparse for Python 2.7

url = “http://media.revsys.com/img/revsys-logo.png”
filename = os.path.basename(urlparse(url).path)
# This returns ‘revsys-logo.png’ from the URL
…

revsys.logo.save(filename, django_file, save=True)