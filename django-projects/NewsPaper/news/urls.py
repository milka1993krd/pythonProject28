from django.urls import path
from .views import NewsList, PostDetail, NewsSearch, PostAdd, PostEdit, PostDelete

urlpatterns = [

    path('', NewsList.as_view()),
    path('<int:pk>', PostDetail.as_view()),
    path('search.html', NewsSearch.as_view()),
    path('add.html', PostAdd.as_view()),
    path('<int:pk>/edit', PostEdit.as_view()),
    path('<int:pk>/delete', PostDelete.as_view())

]

