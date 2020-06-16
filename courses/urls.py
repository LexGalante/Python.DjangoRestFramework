from django.urls import path
from rest_framework.routers import SimpleRouter

from .views import (
    CourseListCreateApiView,
    CourseRetrieveUpdateDestroyApiView,
    ReviewListCreateApiView,
    ReviewRetrieveUpdateDestroyApiView,
    CourseViewSet,
    ReviewViewSet
)

router = SimpleRouter()
router.register('courses', CourseViewSet)
router.register('reviews', ReviewViewSet)

urlpatterns = [
    path('courses/', CourseListCreateApiView.as_view(), name='Courses'),
    path('courses/<int:pk>/',
         CourseRetrieveUpdateDestroyApiView.as_view(), name='Courses'),
    path('courses/<int:course_pk>/reviews',
         ReviewListCreateApiView.as_view(), name='Review of Courses'),
    path('reviews/', ReviewListCreateApiView.as_view(), name='Reviews'),
    path('reviews/<int:pk>/',
         ReviewRetrieveUpdateDestroyApiView.as_view(), name='Reviews'),
]
