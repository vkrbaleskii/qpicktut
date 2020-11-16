from django.urls import path

from . import views

app_name = 'blog'
urlpatterns = [
    path('', views.index, name='index'),
    # path('details/', views.details, name='details'),
    # path('<int:id>/', views.details, name='details'),
    path('posts/<int:id>/details', views.details, name='details'),

]
