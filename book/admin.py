from django.contrib import admin

from .models import Author, Book, BookInstance, Genre

@admin.register(Author)
class AutorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = [
        'first_name',
        'last_name',
        ('date_of_birth', 'date_of_death')
    ]

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BookInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_filter = ('status', 'due_back')
    fieldsets = (
        (None, {
            'fields': (
                'book',
                'imprint'
            )
        }),
        ('Availablity', {
            'fields': (
                'status',
                'due_back'
            )
        })
    )

# @admin.register(Genre)