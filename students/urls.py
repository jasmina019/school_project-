from django.urls import path
from . import views

app_name = 'students'

urlpatterns = [
    path('list/', views.student_list, name='list'),
    path('student/add/', views.student_add, name='add'),
    path('student/detail/<int:pk>/', views.student_detail, name='detail'),
    path('student/delete/<int:pk>/', views.student_delete, name='delete')
]
