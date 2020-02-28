from django.shortcuts import render
from .forms import AddNewBookForm
# Create your views here.
from .objects.Book import Book


def get_book_all(request):
    args = {}
    args['datas'] = [Book("Book1", "Auth1"), Book(
        "Book2", "Auth2"), Book("Book3", "Auth3")]
    args['form'] = AddNewBookForm(request.POST or None)
    if request.method == "POST" and args['form'].is_valid():
        newBook = Book(args['form'].cleaned_data['name_book'],
                       args['form'].cleaned_data['name_author'],
                       args['form'].cleaned_data['detail'])
        args['datas'].append(newBook)
    return render(request, "Components/book.html", args)
