from django.urls import path
from . import views

urlpatterns = [
    path('home/', views.home, name='home'),
    # path('url_name/', views.view_name, name='name'),
    path('about/', views.about, name='about'),
    # path('route/', views.route, name = 'route')
    # route/ - строка, которая содержит URL. Именно с ней маршрутизатор сопоставляет url с запроса
    # views.route - функция определённого route/. Будет автоматически запущена, если какой-то из route подошёл с url запроса
    # name  - имя нашего route, который необходимо использовать при создании ссылки, вместо полного пути (вместо localhost:8000/landing/home)
    path('course/<int:pk>', views.course, name='course'),
    # pk - primary key, тоже самое что id
    # Создаём url "course/int:pk", важно чтобы параметр функции назывался точно также, как и в urls.py
    path('check_leads/', views.check_leads, name='check_leads')
]
