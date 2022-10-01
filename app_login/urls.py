from django.urls import path
from app_login import views

app_name = 'app_login'

urlpatterns = [
    path('signup/',views.sign_up,name='signup' ),
    path('login/',views.login_user,name='login' ),
    path('logout/',views.logout_user,name='logout' ),
    path('profile/',views.user_profile,name='profile' ),
    path('my-products/',views.my_product,name='my_product'),
]
