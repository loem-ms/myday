from django.urls import path
from django.conf.urls import url
from .views import signupview,loginview,NewsList,NewsCreate,NewsUpdate,newsdetailview,NewsDelete,create_comment,TodoList,AssignmentList,TodoCreate,AssignmentCreate,home,TodoUpdate,AssignmentUpdate,TodoDelete,AssignmentDelete,logoutview

urlpatterns = [
    path('signup/', signupview, name='signup'),
    path('login/', loginview, name='login'),
    path('logout/', logoutview, name='logout'),
    path('news/', NewsList.as_view(), name='news'),
    path('createNews/', NewsCreate.as_view(),name='createNews'),
    path('updateNews/<int:pk>', NewsUpdate.as_view(),name='updateNews'),
    path('newsdetail/<int:pk>', newsdetailview, name='newsdetail'),
    path('deleteNews/<int:pk>', NewsDelete.as_view(),name='deleteNews'),
    url("^comment_create/(?P<pk>\d+)/$",create_comment,name='comment_create'),
    path('list/', TodoList.as_view(), name='list'),
    path('',home,name='home'),
    path('assignment/', AssignmentList.as_view(), name='assignment'),
    path('createTodo/', TodoCreate.as_view(),name='createTodo'),
    path('createAssignment/', AssignmentCreate.as_view(),name='createAssignment'),
    path('updateTodo/<int:pk>', TodoUpdate.as_view(),name='updateTodo'),
    path('updateAssignment/<int:pk>', AssignmentUpdate.as_view(),name='updateAssignment'),
    path('deleteTodo/<int:pk>', TodoDelete.as_view(),name='deleteTodo'),
    path('deleteAssignment/<int:pk>', AssignmentDelete.as_view(),name='deleteAssignment'),

]