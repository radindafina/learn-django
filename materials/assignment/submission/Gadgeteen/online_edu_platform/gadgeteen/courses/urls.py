from django.urls import path
from . import views
from students import views as sviews
from django.urls import re_path
from django.contrib.auth import views as auth_views
from django.contrib import admin


urlpatterns = [
     re_path(r'^login/$', auth_views.LoginView.as_view(), name='login'),
    re_path(r'^$', views.index, name='index'),
    re_path(r'^instructor/$', views.ManageCourseListView.as_view(),
         name='instructor'),
    re_path(r'^student/$', sviews.StudentCourseListView.as_view(), name='student'),
    path('mine/',
         views.ManageCourseListView.as_view(),
         name='manage_course_list'),
    path('create/',
         views.CourseCreateView.as_view(),
         name='course_create'),
    path('<pk>/edit/',
         views.CourseUpdateView.as_view(),
         name='course_edit'),
    path('<pk>/delete/',
         views.CourseDeleteView.as_view(),
         name='course_delete'),
    path('<pk>/module/',
         views.CourseModuleUpdateView.as_view(),
         name='course_module_update'),
    path('module/<int:module_id>/content/<model_name>/create/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_create'),
    path('module/<int:module_id>/content/<model_name>/<id>/',
         views.ContentCreateUpdateView.as_view(),
         name='module_content_update'),
    path('content/<int:id>/delete/',
         views.ContentDeleteView.as_view(),
         name='module_content_delete'),
    path('module/<int:module_id>/',
         views.ModuleContentListView.as_view(),
         name='module_content_list'),
    path('module/order/',
         views.ModuleOrderView.as_view(),
         name='module_order'),
    path('content/order/',
         views.ContentOrderView.as_view(),
         name='content_order'),
    path('subject/<slug:subject>/',
         views.CourseListView.as_view(),
         name='course_list_subject'),
    path('<slug:slug>/',
         views.CourseDetailView.as_view(),
         name='course_detail'),
]
