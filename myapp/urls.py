from django.urls import path
from . import views
urlpatterns = [
    path('user/register/',views.sign_up,name='register'),
    path('user/login/',views.user_login,name='login'),
    path('user/logout/',views.logout_user,name='logout'),
    path('',views.index,name='index'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
