# DeviceManagement
Structure: Django + sqlite +  bootstrap3.0 
python2.7 Django1.8

- git clone git@github.com:BensonXiong/DeviceManagement.git
- install python and django environment
- cd DeviceManagement/DeviceManagement
- initial database
  python manage.py makemigrations
  python manage.py migrate
- create superuser
  python manage.py createsuperuser
- (optional) clear the db if it is needed
  python manage.py flush
  python populate_dmanage.py  to insert the test data
- start the server
  python manage.py runserver
- open the url in browser
  http://127.0.0.1:8000/list    or   http:127.0.0.1:8000/admin (login with superuser)



