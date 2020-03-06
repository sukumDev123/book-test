from django.shortcuts import render, redirect
from .forms import AddNewBookForm

# Create your views here.
from .objects.Book import Book
from .presenters.BookPresenters import BookPresenters


def get_book_all(request):
    args = {}
    bookPresenters = BookPresenters()
    args["datas"] = bookPresenters.getAllBooks()
    args["form"] = AddNewBookForm(request.POST or None)

    if request.GET.get("id_edit"):
        id_book = request.GET.get("id_edit")
        book = bookPresenters.getOnceBookByIdBookForUpdate(id_book=id_book)
        args["form"] = AddNewBookForm(request.POST or None, instance=book)

    if request.GET.get("id_delete"):
        id_book = request.GET.get("id_delete")
        args["message"] = bookPresenters.deleteBookByidBook(id_book)

    if request.method == "POST" and args["form"].is_valid():
        args["form"].save()
        args["message"] = (
            "save new book success"
            if not request.GET.get("id_edit")
            else "update book success"
        )
        args["form"] = AddNewBookForm(None)

    return render(request, "Components/book.html", args)
