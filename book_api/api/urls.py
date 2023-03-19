# from django.urls import path
# from .views import BookListView
#
# urlpatterns = [
#     path('', BookListView.as_view()),
#     #path('images/', GalleryView.as_view()),
# ]


from django.urls import path
from .views import AuthorList, AuthorDetail, PublisherList, PublisherDetail, \
    CategoryList, CategoryDetail, BookList, BookDetail, \
    ReviewList, ReviewDetail

urlpatterns = [
    path('authors/', AuthorList.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetail.as_view(), name='author-detail'),
    path('publishers/', PublisherList.as_view(), name='publisher-list'),
    path('publishers/<int:pk>/', PublisherDetail.as_view(), name='publisher-detail'),
    path('categories/', CategoryList.as_view(), name='category-list'),
    path('categories/<int:pk>/', CategoryDetail.as_view(), name='category-detail'),
    path('books/', BookList.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetail.as_view(), name='book-detail'),
    path('reviews/', ReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', ReviewDetail.as_view(), name='review-detail'),
]
