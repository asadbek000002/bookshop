from django.urls import path
from .views import *

urlpatterns = [
    path('', indexView, name='home'),
    path('books/', booksView, name='books'),
    path('detail/<int:pk>/', single, name='details'),
    path('xarid_tarixi/', my_books, name='tarix'),
    path('addremovesaved/<int:pk>', AddRemoveSavedView.as_view(), name='addremovesave'),
    path('saved', SavedView.as_view(), name='saveds')

]