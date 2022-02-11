import csv
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "washu.settings")
django.setup()
path =  "C:\\Users\jnack\dropbox\database project" # Set path of new directory here
os.chdir(path) # changes the directory
from spools.models import Spool # imports the model
Spool.objects.all().delete()
with open('Schedule.csv') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        p = Spool(
            tag=row['Tag'],
            description=row['Descpription'],
            level=row['Level'],
            area=row['Area'],
            PL=row['PL'],
            EL=row['EL'],
            fab_shop=row['Fabrication Shop'],
            spooled_date=row['Spool Date Complete'],
            released_shop=row['Released to Shop/Field'],
            fab_completed=row['Fab Completed'],
            on_site=row['On Site'],
            installed=row['Installed'],
            comments=row['Comments'])
        p.save()

exit()
