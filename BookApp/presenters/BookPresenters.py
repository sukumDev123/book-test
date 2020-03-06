from BookApp.models import BookModel
from BookApp.objects.Book import Book

class BookPresenters:
    def getAllBooks(self):
        return BookModel.objects.all()
    def getOnceBookByIdBook(self , id_book):
        return BookModel.objects.get(id=id_book)
    def saveNewBook(self , body):
        bookObject = Book(name_book=body['name_book'], 
                        name_author=body['name_auth'] , 
                        detail=body['detail'])
        modelBook = BookModel(name_book=bookObject['name_book'], name_author=bookObject['name_author'] , detail=bookObject['detail'])
        modelBook.save()
        return "save new book"
    def updateBook(self , body):
        bookObject = Book(name_book=body['name_book'], 
                        name_author=body['name_auth'] , 
                        detail=body['detail'], 
                        id=body['id'])
        findThisBook = self.getOnceBookByIdBook(bookObject.id)
        findThisBook.name_book = bookObject.name_book
        findThisBook.name_auth = bookObject.name_author
        findThisBook.detail = bookObject.detail
        findThisBook.save()
        return "Update book success"
    
    def deleteBookByidBook(self , id_book):
        book = self.getOnceBookByIdBook(id_book)
        book.delete()
        return "delete success"
