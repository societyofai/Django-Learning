from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('api', views.CourseApiView.as_view()),
    path('add_course', views.AddCourseApiView.as_view()),
]