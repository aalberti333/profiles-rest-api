from django.conf.urls import url
from django.conf.urls import include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register('hello-viewset', views.HelloViewSet, base_name='hello-viewset')

#WHen register a ModelViewset, you don't need to register a base name
router.register('profile', views.UserProfileViewSet)

#base name, since it's not a ModelViewSet
router.register('login', views.LoginViewSet, base_name='login')

router.register('feed', views.UserProfileFeedViewSet)

urlpatterns = [
    url(r'^hello-view/', views.HelloApiView.as_view()),
    url(r'', include(router.urls))
]
