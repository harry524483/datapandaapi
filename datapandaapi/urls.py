from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from rest_framework.urlpatterns import format_suffix_patterns
from login import views

urlpatterns = [
    path('admin/', admin.site.urls),
	url(r'^auth/', views.userAuth),
]
