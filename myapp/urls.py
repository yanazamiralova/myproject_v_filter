from django.urls import path
from django.contrib.auth import views as auth_views
from .views import signup_view, login_view, set_orders
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='myapp/logout.html'), name='logout'),
    path('neworder/', set_orders, name='neworder'),
    path("edit/<int:id>/", views.edit),
    # ...
]
