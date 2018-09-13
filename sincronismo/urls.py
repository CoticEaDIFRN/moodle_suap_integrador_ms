from django.urls import path

from . import views

urlpatterns = [
    path('moodle/create_user', views.create_user_moodle, name='moodle'),
    path('moodle/update_user', views.update_user_moodle, name='moodle'),
    path('moodle/find_user', views.find_user_moodle, name='moodle'),
    path('moodle/create_course', views.create_course, name='moodle'),
    path('moodle/find_course', views.find_course, name='moodle'),
    path('moodle/create_category', views.create_category, name='moodle'),
    path('moodle/find_category', views.find_category, name='moodle'),
]