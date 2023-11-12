from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name = "homepage"),
    path('show_book/',views.showBook, name = "showbook"),
    path('edit_book/<int:id>',views.editBook, name = "editbook"),
    path('delete_book/<int:id>',views.deleteBook, name = "deletebook"),
    path('store_book/',views.storeBook, name = "storebook"),
]
