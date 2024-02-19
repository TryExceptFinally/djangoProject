from rest_framework import serializers
from rest_framework.renderers import JSONRenderer

from .models import Course, Category


class CourseSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=255)
    price = serializers.FloatField()
    students_qty = serializers.IntegerField()
    reviews_qty = serializers.IntegerField()
    created_at = serializers.DateTimeField(read_only=True)
    category_id = serializers.IntegerField()

    # class Meta:
    #     model = Course
    #     fields = ('title', 'price', 'category')


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
