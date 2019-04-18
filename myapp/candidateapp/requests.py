import requests
from django.core.files import File

from .models import Student

r = requests.get(“http://media.revsys.com/img/revsys-logo.png”)

with open(“/tmp/revsys-logo.png”, “wb”) as f:
    f.write(r.content)

reopen = open(“/tmp/revsys-logo.png”, “rb”)
django_file = File(reopen)

revsys = Company()
revsys.name = “Revolution Systems”
revsys.logo.save(“revsys-logo.png”, django_file, save=True)