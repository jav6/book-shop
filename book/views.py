from django.shortcuts import render
from django.views import generic

from .models import Author, Book, BookInstance, Genre

def index(request):
    num_books = Book.objects.all().count()
    num_instance = BookInstance.objects.all().count()
    num_instance_available = BookInstance.objects.filter(status__exact = 'a').count()
    num_author = Author.objects.count()
    context = {
        'num_books': num_books,
        'num_instance': num_instance,
        'num_instance_available': num_instance_available,
        'num_author': num_author,
    }
    return render(request, 'book/index.html', context)

class BookListView(generic.ListView):
    model = Book
    context_object_name = 'my_book_list'
    template_name = 'book/book_list.html'
    # queryset = Book.objects.filter(title__icontains = 'django')[:5]