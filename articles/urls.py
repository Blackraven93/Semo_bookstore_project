<<<<<<< HEAD
from django.urls import path
from . import views
app_name = 'articles'

urlpatterns = [
    path("author/",views.ThisMonthAuthorListView ,name="author"),
    # path("book/",views. ,name="book"),
    # path("event/",views. ,name="event"),
=======
from django.urls import path

app_name = 'articles'

urlpatterns = [

>>>>>>> ade7bc9c06408908f88500ba8c9a11e47d237983
]