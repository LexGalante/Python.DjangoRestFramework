from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from .models import Course, Review
from .serializers import CourseSerializer, ReviewSerializer


class CourseApiView(APIView):
    def get(self, request):
        courses = Course.objects.all()
        serializer = CourseSerializer(courses, many=True)

        return Response({
            'status': True,
            'message': 'Success!!!',
            'data': serializer.data
        })

    def post(self, request):
        serializer = CourseSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': True,
            'message': 'Success!!!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)


class ReviewApiView(APIView):
    def get(self, request):
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)

        return Response({
            'status': True,
            'message': 'Success!!!',
            'data': serializer.data
        })

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': True,
            'message': 'Success!!!',
            'data': serializer.data
        }, status=status.HTTP_201_CREATED)
