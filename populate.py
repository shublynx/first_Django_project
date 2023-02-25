import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE","first_project.settings")

import django
django.setup()


import random
from firstapp.models import Accessrecord,Webpage,Topic
from faker import Faker

fakegen = Faker()
topics = ['Search','Social','Marketplace','News','Games']

def add_topic():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t
def populate(N=5):

    for entry in range(N):
# create topic for entry
        topicname = add_topic()

# create webpage objects
        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()

        webpage_entry = Webpage.objects.get_or_create(topic=topicname,name=fake_name,url=fake_url)[0]
        access_record = Accessrecord.objects.get_or_create(name=webpage_entry,date=fake_date)[0]

if __name__ == "__main__":
    print("populating script")
    populate(20)
    print("populating complete")