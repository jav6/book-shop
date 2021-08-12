from django.shortcuts import render
from django.views import generic
from django.db.models import Q

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
    paginate_by = 3
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        
        context['my_book_list'] = Book.objects.all()
        
        return context

class BookDetailView(generic.DetailView):
    model = Book

class AuthorListView(generic.ListView):
    model = Author

class SearchResultsView(generic.ListView):
    model = Book
    paginate_by = 2
    template_name = 'book/search_results.html'
    def get_queryset(self):
        if self.request.GET.get('q'):
            query = self.request.GET.get('q')
        else:
            query = ''
        object_list = Book.objects.filter(
            Q(title__icontains=query) | Q(summary__icontains=query)
        )
        return object_list