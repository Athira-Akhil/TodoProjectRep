from . import views
from django.urls import path

urlpatterns = [

    path('',views.addtask,name='addtask'),
    path('delete/<int:taskid>/',views.delete,name='delete'),
    path('update/<int:taskid1>/',views.updatetask,name='updatetask'),
    path('cbvhome/',views.TaskListView.as_view(),name='cbvhome'),
    path('cbvdetail/<int:pk>/',views.TaskDetailView.as_view(),name='cbvdetail'),
    path('cbvupdate/<int:pk>/',views.TaskUpdateview.as_view(),name='cbvupdate'),
    path('cbvdelete/<int:pk>/',views.TaskDeleteview.as_view(),name='cbvdelete'),

]