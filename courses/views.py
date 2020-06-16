from rest_framework import generics
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from .models import Course, Review
from .permissions import IsMasterUser
from .serializers import CourseSerializer, ReviewSerializer

""" 
v1
"""


class CourseListCreateApiView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ReviewListCreateApiView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        if self.kwargs.get('course_pk'):
            return self.queryset.filter(course_id=self.kwargs.get('course_pk'))

        return self.queryset.all()


class ReviewRetrieveUpdateDestroyApiView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


"""
v2 
"""


class CourseViewSet(viewsets.ModelViewSet):
    permissions_classes = (
        IsMasterUser,
        permissions.DjangoModelPermissions)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    @action(detail=True, methods=['GET'])
    def reviews(self, request, pk=None):
        self.pagination_class.page_size = 5
        reviews = Review.objects.filter(course_id=pk)
        page = self.paginate_queryset(reviews)

        if page is not None:
            serializer = ReviewSerializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data)


class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
