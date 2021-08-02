from django.urls import path

from . import views

app_name = 'book'
urlpatterns = [
    path('', views.index, name='index'),
    path('list/', views.BookListView.as_view(), name='bookList'),
    path('detail/<int:pk>', views.BookDetailView.as_view(), name='bookDetail'),
]