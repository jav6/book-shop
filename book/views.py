from django.shortcuts import render

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