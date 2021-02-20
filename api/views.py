from django.shortcuts import get_object_or_404
from django.db.utils import IntegrityError
from rest_framework import viewsets, serializers
from rest_framework.permissions import (IsAuthenticatedOrReadOnly,)
from rest_framework.pagination import PageNumberPagination


from .models import Review, Title
from .serializers import (ReviewSerializer, CommentSerializer)


class ReviewViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        return title.reviews

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        try:
            serializer.save(title=title)
        except IntegrityError:
            message = 'Можно оставить только один отзыв на один объект.'
            raise serializers.ValidationError(message)


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticatedOrReadOnly, ]
    pagination_class = PageNumberPagination

    def get_queryset(self):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        review = get_object_or_404(Review,
                                   title=title,
                                   id=self.kwargs.get('review_id'))
        return review.comments

    def perform_create(self, serializer):
        title = get_object_or_404(Title, id=self.kwargs.get('title_id'))
        review = get_object_or_404(Review,
                                   title=title,
                                   id=self.kwargs.get('review_id'))
        serializer.save(review=review)
