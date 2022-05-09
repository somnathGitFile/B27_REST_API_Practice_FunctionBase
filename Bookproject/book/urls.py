from django.urls import path
from.import views

urlpatterns=[
    path('bkk/', views.BookDetails.as_view()),
    path('bkk/<int:id>/', views.BookInfo.as_view())
]