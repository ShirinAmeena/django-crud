from django.urls import path
from . import views
urlpatterns = [
   
    path('', views.index,name='index'),
    path('list/', views.list,name='list'),
    path('student/', views.student,name='student'),
    path('edit_student/<int:student_id>/', views.edit_student, name='edit_student'),  # Ensure the URL pattern accepts an integer argument
    path('delete_student/<int:student_id>/', views.delete_student, name='delete_student'),
]