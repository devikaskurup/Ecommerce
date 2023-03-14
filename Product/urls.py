from django.urls import path
from.import views

urlpatterns = [
    path("Addproducts",views.Addproducts,name="Addproducts"),
    path("ProductViewMerchant",views.ProductViewMerchant,name="ProductViewMerchant"),
    path("DeleteProduct/<int:pk>",views.DeleteProduct,name="DeleteProduct"),
    path("updateproduct/<int:pk>",views.updateproduct,name="updateproduct"),
    path("viewproduct/<int:pk>",views.viewproduct,name="viewproduct"),
    
    
]
