from django.urls import path,include
from .views import PostList, PostDetail, UserList, UserDetail
# from rest_framework import routers

# router = routers.DefaultRouter()

# router.register('users',UserViewSet, basename='users')

urlpatterns = [
    path("", PostList.as_view(), name='post_list'),
    path("<int:pk>/", PostDetail.as_view(), name='post_detail'),
    path("users/", UserList.as_view()),
    path("users/<int:pk>/", UserDetail.as_view()), 
]

