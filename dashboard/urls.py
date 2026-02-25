from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('signup/', views.signup_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('dashboard/', views.dashboard_home),
    path('analytics/', views.analytics_page),
    path('complete-task/<int:task_id>/', views.complete_task),
    path('delete-task/<int:task_id>/', views.delete_task),
    path('edit-task/<int:task_id>/', views.edit_task),
]