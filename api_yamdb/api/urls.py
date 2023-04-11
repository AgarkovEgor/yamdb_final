from api.views import (CategoryViewSet, CommentViewSet, GenreViewSet,
                       ReviewViewSet, TitleViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from users.views import UserViewSet, signup, token

router = DefaultRouter()
router.register('users', UserViewSet)
router.register('titles', TitleViewSet, basename='titles')
router.register('categories', CategoryViewSet)
router.register('genres', GenreViewSet)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments')
router.register(r'titles/(?P<title_id>\d+)/reviews',
                ReviewViewSet, basename='reviews')

authurls = [
    path('token/', token, name='token_obtain'),
    path('signup/', signup, name='signup'),
]


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/auth/', include(authurls))
]
