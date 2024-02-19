from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:course_id>', views.single_course, name='single_course'),
    path('api/v1/courses/', views.CourseAPIView.as_view(), name='api_v1_courses'),
    path('api/v1/categories/', views.CategoryAPIView.as_view(), name='api_v1_categories')
]