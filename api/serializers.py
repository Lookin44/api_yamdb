from django.db.models import Avg
from django.shortcuts import get_object_or_404
from rest_framework import serializers

from users.models import User

from .models import Category, Comment, Genre, Review, Title


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Category


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ['name', 'slug']
        model = Genre


class CategorySlugRelatedField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        return CategorySerializer().to_representation(obj)


class GenreSlugRelatedField(serializers.SlugRelatedField):
    def to_representation(self, obj):
        return GenreSerializer().to_representation(obj)


class TitleSerializer(serializers.ModelSerializer):
    category = CategorySlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )
    genre = GenreSlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True,
    )
    rating = serializers.SerializerMethodField()

    class Meta:
        fields = '__all__'
        model = Title

    @staticmethod
    def get_rating(obj):
        return obj.reviews.aggregate(rating=Avg('score'))['rating']


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
        slug_field='username',
    )

    title = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='id'
    )

    class Meta:
        fields = '__all__'
        model = Review

    def validate(self, data):
        if self.context['request'].method == 'POST':
            title = get_object_or_404(
                Title, pk=self.context['view'].kwargs.get('title_id'))
            author = self.context['request'].user
            if Review.objects.filter(
                title_id=title,
                author=author,
            ).exists():
                raise serializers.ValidationError(
                    'Можно оставить только один отзыв на один объект.'
                )
        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        default=serializers.CurrentUserDefault(),
        queryset=User.objects.all(),
        slug_field='username',
    )
    review = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='text'
    )

    class Meta:
        fields = '__all__'
        model = Comment
