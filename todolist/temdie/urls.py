from django.urls import path
from . import views

urlpatterns=[
    path('signup/', views.signup, name="signup"),
    path('login/', views.login, name='login'),
    path('updatestatus/<int:task_id>/', views.updatestatus, name='update_status'),
    path('addtask/<int:user_id>/', views.addtask, name='add_task'),
    path('deletetask/<int:task_id>/', views.deletetask, name='delete_task'),
    path('addtag/', views.addtag, name='add_tag'),

] 