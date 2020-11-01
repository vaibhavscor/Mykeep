from django.urls import path
from .import views


urlpatterns = [
    path('',views.writepad,name="home_page"),
    path('read/<str:id>',views.readNote,name="note_read"),
    path('read/edit_note/<str:id>',views.editNote,name="edit_note"),
    path('read/delete_note/<str:id>',views.deleteNote,name="delete_note"),
    path('search',views.searchNote,name='search'),

]
