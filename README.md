# amis-demo-web

pip freeze > requirements.txt

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver 8080

在apps/amis/views.py中添加新页面json
在apps/amis/urls.py中添加新页面链接
在apps/amis/site.py中添加新页面路由