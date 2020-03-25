from django.urls import path
from . import views

urlpatterns = [
    path('threadlist/', views.threadlist, name='threadlist'),
    path('createthread/', views.createthread, name='createthread'),
    path('threadcontent/<int:id>',views.threadcontent,name='threadcontent'),
    path('thread_deleterequest/',views.thread_deleterequest,name='thread_deleterequest'),
    path('threadcontent_delrequest/',views.threadcontentrequest,name='threadcontent_deleterequest'),
    path('manager_login/',views.manager_login,name='manager_login'),
    path('manager_page/',views.manager_page,name='manager_page'),
]