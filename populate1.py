import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django
django.setup()


import random
from firstapp.models import Accessrecord,Webpage,Topic,User
from faker import Faker

fakegen = Faker()

def populate(N=5):
    for i in range(N):
        fake_fname = fakegen.first_name()
        fake_lname = fakegen.last_name()
        fake_email = fakegen.email()

        users_entry = User.objects.get_or_create(fname=fake_fname, lname=fake_lname, email=fake_email)[0]

if __name__ == "__main__":
    populate(40)