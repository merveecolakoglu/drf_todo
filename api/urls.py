from django.urls import path

from . import views
from .views import TaskListView, TaskCreateView, TaskDetailView, TaskDeleteView

urlpatterns = [
    path('',views.apiOwerview, name='api-overview'),

    path('task-list/',TaskListView.as_view(),name='task-list'),
    path('task-detail/',TaskDetailView.as_view(),name='task-detail'),
    path('task-create/',TaskCreateView.as_view(),name='task-create'),

    path('task-update/<str:pk>/',views.taskUpdate,name='task-update'),
    path('task-delete/<str:pk>/',TaskDeleteView.as_view(),name='task-delete'),
]