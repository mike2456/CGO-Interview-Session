from django.contrib import admin
from django.urls import path
from . import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('assignment/', views.CGO_Interview_Session.as_view(), name='assignment')
]
