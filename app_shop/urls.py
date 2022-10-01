from django.urls import path
from app_shop import views
app_name = 'app_shop'
urlpatterns = [
    path('',views.Home.as_view(),name='home' ),
    path('product/<pk>/',views.Post,name='product' ),
    path('edit/<pk>/',views.Updateview.as_view(),name='edit_products'),
    path('add-product/',views.Createview.as_view(),name='add_product'),
    # path('product/<pk>/',views.Post.as_view(),name='product')
]
