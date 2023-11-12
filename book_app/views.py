from django.shortcuts import render,redirect
from book_app.forms import BookStoreForm
from book_app.models import BookStoreModel
# Create your views here.


def home(request):
    return render(request,"./book_app/home.html")


def storeBook(request):
    if request.method == 'POST':
        book = BookStoreForm(request.POST)
        if book.is_valid():
            print(book.cleaned_data)
            book.save(commit=True)
            
    else:
        book = BookStoreForm()
    return render(request,"./book_app/store_book.html",{'form': book})


def showBook(request):
    book = BookStoreModel.objects.all()
    print(book)
    return render(request,"./book_app/show_book.html",{'data':book})

def editBook(request,id):
    book = BookStoreModel.objects.get(pk = id)
    form = BookStoreForm(instance = book)
    if request.method == 'POST':
        form =BookStoreForm(request.POST, instance = book)
        if form.is_valid():
            form.save(commit=True)
            return redirect("showbook")
    return render(request,"./book_app/store_book.html",{'form':form})


def deleteBook(request,id):
    book = BookStoreModel.objects.get(pk = id).delete()
    return redirect('showbook')
    