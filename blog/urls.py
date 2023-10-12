from django.urls import path
from . import views
from .views import HelloWorld

urlpatterns = [
    path('blog', views.hello_world),
    path('blog/cbv', views.HelloWorld.as_view()),
    path('crypto', views.GetCryptoPrice.as_view()),
    path('articles', views.ArticleListView.as_view()),
    path('articles/<int:pk>', views.ArticleDetailView.as_view()),
]