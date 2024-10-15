from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),  
    path('about/', views.about, name='about'),
    path('letter/', views.letter_index, name='letter_index'),
    path('letter/create/', views.letter_create, name='letter_create'),
    path('letter/update/<int:letter_id>/', views.letter_update, name='letter_update'),
    path('letter/delete/<int:letter_id>/', views.letter_delete, name='letter_delete'),
]