from django.shortcuts import render, redirect
from .models import Book, Author
def index(request):
    
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "index.html", context)

def index2(request):
    context = {
        "all_books": Book.objects.all(),
        "all_authors": Author.objects.all()
    }
    return render(request, "addauthors.html", context)

def processbook(request):
    booktitle = request.POST['booktitle']
    bookdesc = request.POST['bookdesc']
    # bookId = Book.objects.get(id=request.POST) ????
    newBook = Book.objects.create(title = booktitle, desc = bookdesc)
    return redirect("/")

def processauthor(request):
    authorFname = request.POST['authorFname']
    authorLname = request.POST['authorLname']
    notes = request.POST['notes']
    
    newAuthor = Author.objects.create(first_name = authorFname, last_name = authorLname, notes = notes)
    return redirect("/addauthors")

def viewBook(request, bookId):
    context = {
        "book": Book.objects.get(id = bookId),
        "all_authors": Author.objects.all()
    }
    return render(request, "viewbook.html", context)

def addbook(request, authorId):
    authorObject = Author.objects.get(id = authorId)
    
    authorObject.books.add(Book.objects.get(id = request.POST['bookId']))
    
    return redirect(f"/viewauthor/{authorId}")

def addauthor(request, bookId):
    bookObject = Book.objects.get(id = bookId)
    bookObject.authors.add(Author.objects.get(id = request.POST['authorId']))
    
    return redirect(f"/viewbook/{bookId}")

def viewAuthor(request, authorId):
    context = {
        "author" : Author.objects.get(id = authorId),
        "all_books": Book.objects.all()
    }
    return render(request, "viewauthor.html", context)
