from django.contrib import admin
from django.urls import path
from .views import ModelView
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ModelView.as_view(), name='index'),
]
