from django.urls import path
from . import views
from .views import HelloWorld
from rest_framework.authtoken import views as token_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

urlpatterns = [
    path('blog', views.hello_world),
    path('blog/cbv', views.HelloWorld.as_view()),
    path('crypto', views.GetCryptoPrice.as_view()),
    path('articles', views.ArticleListView.as_view()),
    path('articles/<int:pk>', views.ArticleDetailView.as_view()),
    path('articles/add', views.AddArticleView.as_view()),
    path('articles/update/<int:pk>', views.ArticleUpdateView.as_view()),
    path('articles/delete/<int:pk>', views.ArticleDeleteView.as_view()),
    path('check', views.CheckToken.as_view()),
    # path('login/', token_views.obtain_auth_token),
    path('article/comments/<int:pk>', views.ArticleCommentsView.as_view()),
    path('users', views.UserDetailView.as_view()),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]

# router = DefaultRouter()
# router.register(r'articles/viewset', views.ArticleViewSet, basename='articles')
# urlpatterns += router.urls
