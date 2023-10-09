from django.urls import path
from . import views
from .views import HelloWorld

urlpatterns = [
    path('blog', views.hello_world),
    path('blog/cbv', views.HelloWorld.as_view()),
]