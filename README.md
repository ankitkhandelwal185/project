
#project setup
pip install django psycopg2
python manage.py makemigrations
python manage.py migrate

python manage.py createsuperuser

python manage.py runserver 0.0.0.0:8000

#api 

login api -> http://localhost:8011/api/login
POST request, no headers required 
payload -> 
{
	"username":"ankit",
	"password": "ankit1234"
}


create article -> http://localhost:8011/api/article/create
POST request, add Autherization token in headers with value -> 'token key'
payload ->
{
	"headline": "ankit",
	"content": "ankit"
}


update article -> http://localhost:8011/api/article/update
POST request, add Autherization token in headers with value -> 'token key'
payload ->
{
	"headline": "ankit",
	"content": "ankit"
}


article detail -> http://localhost:8011/api/article/detail?articleId=1234
GET request
