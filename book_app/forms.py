from django import forms 
from . models import BookStoreModel

class BookStoreForm(forms.ModelForm):
    class Meta:
        model = BookStoreModel
        fields = '__all__'
        labels = {
            'id' : 'ID',
            'book_name' : 'Book_name',
            'author' : 'Author_name',
            'category' : 'Category',
            'first_pub' : 'First_Publis',
            'last_pub' : 'Last_Publis'
        }
        
        help_texts = {
            'id' : 'Enter a book  id',
            'book_name' : 'Enter describe a book name',
            'author' : 'Enter author name',
            'category' : 'Select a category name',
            'first_pub' : 'Enter first publication',
            'last_pub' : 'Enter last publication'
            
        }