from rest_framework import serializers
from django.db.models import Avg

from .models import Course, Review


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        extra_kwargs = {
            'email': {'write_only': True}
        }
        model = Review
        fields = (
            'id',
            'name',
            'email',
            'text',
            'note',
            'created_at',
            'updated_at',
            'active'
        )

    def validate_note(self, value):
        if value in range(1, 6):
            return value

        return serializers.ValidationError('A Nota da curso deve estar entre 1 ~ 5')


class CourseSerializer(serializers.ModelSerializer):
    # Nested
    #reviews = ReviewSerializer(many=True, read_only=True)

    # HyperlinkedRelatedField
    # reviews = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='review-detail'
    # )

    # Primary Key
    reviews = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    mean = serializers.SerializerMethodField()

    class Meta:
        model = Course
        fields = (
            'id',
            'title',
            'url',
            'created_at',
            'updated_at',
            'active',
            'reviews',
            'mean'
        )

    def get_mean(self, obj):
        mean = obj.reviews.aggregate(Avg('note')).get('review__avg')
        if mean is None:
            return 0

        return round(mean * 2) / 2
