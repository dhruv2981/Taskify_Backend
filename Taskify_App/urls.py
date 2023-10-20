from rest_framework import routers
from Taskify_App.views import *
from django.urls import include,path


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('lists',ListViewSet)
router.register('cards',CardViewSet)
router.register('projects',ProjectViewSet)
router.register('notifications',NotificationViewSet)
router.register('logs',LogViewSet)
router.register('comments',CommentViewSet)
router.register('project_roles',Project_roleViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('auth/', include('rest_framework.urls')),
    path('oauth/callback/',OauthCallback.as_view()),
    # path('open_auth/callback/',OauthCallback.as_view()),

   
    
]
