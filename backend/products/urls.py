from django.urls import path
from . import views 
from . import view

#/api/
urlpatterns =[
    path("list/", views.product_list_create_view),                 #views.product_alt_view
    path("<int:pk>/", views.ProductDetailAPIView.as_view()),  #views.product_alt_view
    path("<int:pk>/update/", views.product_update_view),
    path("<int:pk>/delete/", views.product_delete_view),
    path("", views.product_mixins_view),   
    
    path('test', view.api_test)   #"api/test"
]