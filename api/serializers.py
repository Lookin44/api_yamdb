from django.db.models import Avg
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
            if 'score' in data:
                if data['score'] not in range(1, 11):
                    raise serializers.ValidationError(
                        "Рейтинг должен быть от 1 до 10")
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
