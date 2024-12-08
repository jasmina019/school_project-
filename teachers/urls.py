from django.urls import path
from . import views

app_name = 'teachers'

urlpatterns = [
    path('list/', views.teacher_list, name='list'),
    path('teacher_add/', views.teacher_add, name='add'),
    path('teacher/detail/<int:pk>/', views.teacher_detail, name='detail'),
    path('teacher/delete/<int:pk>/', views.teacher_delete, name='delete')
]