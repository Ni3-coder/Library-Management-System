from django.urls import URLPattern, path
from book import views

urlpatterns = [
    path('index/', views.index),
    path('home/', views.home),
    path('signup/', views.signup),
    path('list/', views.list),
    path('aupdate/', views.aupdate),
    path('addbook/', views.abook),
    path('detail/<int:id>/', views.detail),
    path('bupdate/<int:id>/', views.bupdate),
    path('delete/<int:id>/', views.delete)
]
