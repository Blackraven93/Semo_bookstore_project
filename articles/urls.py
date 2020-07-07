from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path("author/",views.ThisMonthAuthorListView ,name="author"),
    # path("book/",views. ,name="book"),
    # path("event/",views. ,name="event"),
]