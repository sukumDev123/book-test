from django.shortcuts import render

# Create your views here.


def get_book_all(request):
    return render(request, "Components/book.html")
