from rest_framework import serializers

from .models import Category, Genre, Title


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

    class Meta:
        fields = '__all__'
        model = Title
