"""
URL configuration for django_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from scavenger import views
from django.urls import include, path, re_path
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.main_page, name='main_page'),
    path('', views.splash_screen, name='splash'),
    path('scan_qr_validation/', views.scan_qr_validation, name='scan_qr_validation'),
    path('instructions/', views.instructions_page, name='instructions_page'),
    path('socmaps/', views.socmaps_page, name='socmaps_page'),
    path('scan_redeem_check/', views.scan_redeem_check, name='scan_redeem_check'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
