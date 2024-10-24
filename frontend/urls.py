from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('', views.user_login, name='login'),
    path('signup/', views.user_signup, name='signup'),
    path('profile/', views.user_profile, name='profile'),
    path('profile-update/', views.profile_update, name='profile-update'),
    path('logout/', views.user_logout, name='logout'),
    path('orders/', views.order_list, name='order_list'),
    path('admin_dashboard/', views.admin_dashboard, name='admin-dashboard'),
    path('staff_dashboard/', views.staff_dashboard, name='staff-dashboard'),
    path('update-order/<int:order_id>/', views.update_order, name='update_order'),
]
