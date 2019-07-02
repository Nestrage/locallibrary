from django.urls import path

from library_app.views import (
    AuthorCreate,
    AuthorDetail,
    BookCreate,
    BookDetail,
    SaleCreate,
    SaleDetail
)

urlpatterns = [
    path("authors", AuthorCreate.as_view()),
    path("authors/<int:pk>", AuthorDetail.as_view()),
    path("books", BookCreate.as_view()),
    path("books/<int:pk>", BookDetail.as_view()),
    path("sales", SaleCreate.as_view()),
    path("sales/<int:pk>", SaleDetail.as_view())
]