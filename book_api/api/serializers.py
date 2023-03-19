# from rest_framework import serializers
# from .models import Book
#
#
# class BookSerializer(serializers.ModelSerializer):
#     image = serializers.ImageField(max_length=None, use_url=True)
#
#     class Meta:
#         model = Book
#         fields = ['title', 'author', 'image']
#
#


from rest_framework import serializers
from .models import Author, Publisher, Category, Book, Review


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class BookSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    author = AuthorSerializer()
    publisher = PublisherSerializer(many=False)
    cover_image = serializers.ImageField(max_length=None, use_url=True)

    class Meta:
        model = Book
        fields = ['title', 'author', 'publisher', 'cover_image', 'categories', 'publisher']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'
