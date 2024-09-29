from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('alumni/', views.alumni_view, name='alumni_url'),
    path('alumni/details/<int:id>', views.details, name='details'),
    path('alumni/items/', views.items, name='items'),  
    path('alumni/leased_view/', views.leased_view, name='leased_view'),
    path('alumni/leased_view/leased_details/<int:id>', views.leased_details, name='leased_details'),
    #path('my_redirect', views.my_redirect, name='my_redirect'),  



    path('alumni/book_view/', views.book_view, name='book_view'),
    path('alumni/book_view/book_details/<int:id>', views.book_details, name='book_details'),
    path('alumni/extra/', views.extra, name='extra'),

    path('alumni/pdf_view/', views.pdf_view, name='pdf_view'),



       

]