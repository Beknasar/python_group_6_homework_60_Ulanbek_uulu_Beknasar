"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from webapp.views import IndexView, TaskCreateView, TaskDeleteView, TaskView, TaskUpdateView, \
    ProjectView, ProjectCreateView, TaskListView, ProjectUpdateView, ProjectDeleteView, ProjectPermissonUpdateView
from django.contrib.auth.views import LoginView, LogoutView
# from accounts.views import login_view, logout_view


urlpatterns = [
    path('admin/', admin.site.urls),

    path('', IndexView.as_view(), name='index'),
    path('project/', include([
        path('<int:pk>/', ProjectView.as_view(), name='project_view'),
        path('add/', ProjectCreateView.as_view(), name='project_create'),
        path('<int:pk>/update', ProjectUpdateView.as_view(), name='project_update'),
        path('<int:pk>/delete', ProjectDeleteView.as_view(), name='project_delete'),
        path('<int:pk>/tasks/add/', TaskCreateView.as_view(), name='task_create'),
        path('<int:pk>/edit_user', ProjectPermissonUpdateView.as_view(), name='project_user_edit')
    ])),

    path('tasks/', TaskListView.as_view(), name='task_list'),
    path('tasks/<int:pk>/', TaskView.as_view(), name='task_view'),
    path('tasks/<int:pk>/delete/', TaskDeleteView.as_view(), name='task_delete'),
    path('tasks/<int:pk>/update/', TaskUpdateView.as_view(), name='task_update'),

    path('accounts/', include('accounts.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
