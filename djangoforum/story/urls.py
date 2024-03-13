from django.urls import path

from . import views

app_name = 'story'

urlpatterns = [
    path('creat/', views.creat, name='creat'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/vote/', views.vote, name='vote'),
]