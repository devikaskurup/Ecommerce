from django.shortcuts import render,redirect
from.forms import productAddform
from django.contrib import messages
from.models import ProductDetails

from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required(login_url="SignIn")
def Addproducts(request):
    form = productAddform()
    if request.method=="POST":
        form = productAddform(request.POST,request.FILES)
        if form.is_valid():
            product = form.save()
            product.merchant = request.user
            product.save()
            messages.info(request,"Product Added To list")
            return redirect('Addproducts')
        
    return render(request,"addproduct.html",{"form":form})

@login_required(login_url="SignIn")
def ProductViewMerchant(request):
    products = ProductDetails.objects.all()
    context ={
        "products":products
    }
    return render(request,"productlistview.html",context)

@login_required(login_url="SignIn")
def DeleteProduct(request,pk):
    product = ProductDetails.objects.get(productId = pk)
    product.product_image.delete()
    product.delete()
    messages .info(request,"product deleted")
    return redirect("ProductViewMerchant")

@login_required(login_url="SignIn")
def updateproduct(request,pk):
    product=ProductDetails.objects.filter(productId=pk)
    if request.method == "POST":
        
       
        pname = request.POST["pname"]
        pbrand = request.POST["pbrand"]
        pdisc = request.POST["pdisc"]
        pstock = request.POST["pstock"]
        pcat = request.POST["pcat"]
        price = request.POST["price"]
        image = request.FILES["image"]
        
        item = ProductDetails.objects.get(productId=pk)
        
        item.produc_tName =pname
        item.product_Brand =pbrand
        item.product_Discription =pdisc
        item. product_price= price
        item.product_category =pcat
        item.product_stock =pstock
        item.product_image.delete()
        item.product_image = image
        item.save()
        messages.info(request,"item updated")
        return redirect("updateproduct",pk=pk)
    context={
        "product":product
    }
    return render(request,"updateproduct.html",context)

def viewproduct(request,pk):
    product=ProductDetails.objects.filter(productId=pk)
    context = {
        "product":product
    }
    return render(request,"viewproduct.html",context)

def CartView (request):
    return render(request,"cart.html")