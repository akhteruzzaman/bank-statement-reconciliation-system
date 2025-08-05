from django.contrib import admin
from django.urls import path
from hello.views import hello_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', hello_view),
]
