from django.forms import model_to_dict
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from rest_framework import generics
from rest_framework.response import Response

from .models import Course, Category
from .serializers import CourseSerializer, CategorySerializer


def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {"courses": courses})


def single_course(request, course_id):
    # # OPTION 1
    # try:
    #     course = Course.objects.get(pk=course_id)
    #     return render(request, 'shop/single_course.html', {"course": course})
    # except Course.DoesNotExist:
    #     raise Http404("Course not found!")

    # OPTION 2
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {"course": course})


# class CourseAPIView(generics.ListAPIView):
#     queryset = Course.objects.all()
#     serializer_class = CourseSerializer

class CourseAPIView(generics.GenericAPIView):
    def get(self, request):
        c = Course.objects.all()
        return Response({'posts': CourseSerializer(c, many=True).data})

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        post_new = Course.objects.create(
            title=request.data['title'],
            price=request.data['price'],
            students_qty=request.data['students_qty'],
            reviews_qty=request.data['reviews_qty'],
            category_id=request.data['category_id'],
        )
        return Response({'post': CourseSerializer(post_new).data})

    serializer_class = CourseSerializer


class CategoryAPIView(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
