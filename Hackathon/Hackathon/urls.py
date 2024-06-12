from django.contrib import admin
from django.urls import path

from App1.views import IndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView)
]
