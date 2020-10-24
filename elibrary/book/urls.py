from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AuthorViewsets, BookViewsets

app_name = 'book'
router = DefaultRouter()
router.register('author', AuthorViewsets)
router.register('book', BookViewsets)

urlpatterns = [
    path('', include(router.urls)),
]
