from django.urls import path
from . import views

urlpatterns = [
    path('',views.apiOwerview, name='api-overview'),
    path('task-list/',views.taskList,name='task-list'),
    path('task-detail/',views.taskDetail,name='task-detail'),
    path('task-create/',views.taskCreate,name='task-create'),

    path('task-update',views.taskUpdate,name='task-update'),
    path('task-delete',views.taskDelete,name='task-delete'),
]