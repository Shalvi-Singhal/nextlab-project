from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'apps', views.AppViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'task-completions', views.TaskCompletionViewSet)

urlpatterns = [
    path('myview/', views.my_view, name='my_view'),
    path('', views.home, name='home'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('logout/', views.signout, name='logout'),
    path('apps/', views.apps_list, name='apps_list'),
    path('apps/<int:app_id>/', views.app_detail, name='app_detail'),
    path('tasks/<int:task_id>', views.task_submit, name='task_submit'),
    path('add_app/', views.add_app, name='add_app'),
    path('save_app/', views.save_app, name='save_app'),

    path('api/', include(router.urls)),
]


