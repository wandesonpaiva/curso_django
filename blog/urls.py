from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('posts', views.PostModelViewSet)

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('api/v1', include(router.urls))
]