from django.contrib import admin
from django.urls import path,include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('app_shop.urls')),
    path('account/',include('app_login.urls')),
    path('shop/',include('app_order.urls')),
    path('payment/',include('app_payment.urls')),
    path('summernote/', include('django_summernote.urls')),

]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)