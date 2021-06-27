
from django.urls import path
from .views import Home,SearchA,SearchC


urlpatterns = [
    path('', Home.as_view()),
    path('search/', SearchA.as_view(),name='templates'),
    path('searchC/', SearchC.as_view(),name='templat')
]