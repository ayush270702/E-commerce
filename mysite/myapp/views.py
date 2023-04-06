from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.core.paginator import Paginator

from .models import Product






def index(request):
    return HttpResponse("Hello!!!!!!!!!!!!!!!!!!!!!!")



# ------------------------------------------ Products -------------------------------------------------------------------------
# function based view
def products(request):
    page_obj = products = Product.objects.all()
    
    
    product_name = request.GET.get('product_name')
    
    if product_name!='' and product_name!=None:
        page_obj = products.filter(name__icontains=product_name)
    
    paginator = Paginator(page_obj,3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj' : page_obj
    }

    return render(request, 'myapp/index.html', context)

#class based view
class ProductListView(ListView):
    model = Product
    template_name = 'myapp/index.html'
    context_object_name = 'products'
    paginate_by = 3
# ---------------------------------------------------------------------------------------------------------------------  





# ------------------------------------------ Product Detail -------------------------------------------------------------------------  
#function based view
def product_detail(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product' : product
    }
    return render(request,'myapp/product_detail.html',context)    

#class based view
class ProductDetailView(DetailView):
    model = Product
    template_name = 'myapp/product_detail.html'
    context_object_name = 'product'
# ---------------------------------------------------------------------------------------------------------------------      



# ------------------------------------------ Add Product -------------------------------------------------------------------------
#function based view
@login_required
def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        description = request.POST.get('description')
        image = request.FILES['upload']
        seller = request.user

        product = Product(name=name, price=price, description=description, image=image, seller_name = seller)
        product.save()

        return redirect('/myapp/product')


    return render(request, 'myapp/addproduct.html')    
# ---------------------------------------------------------------------------------------------------------------------      




# ------------------------------------------ Update Product -------------------------------------------------------------------------
def update_product(request,pk):

    product = Product.objects.get(pk=pk)
    if request.method=='POST':
        product.name = request.POST.get('name')
        product.price = request.POST.get('price')
        product.description = request.POST.get('description')
        product.image = request.FILES['upload']

        product.save()
        return redirect('/myapp/product')

    context = {
        'product':product
    }
    return render(request, 'myapp/updateproduct.html',context)    
# ---------------------------------------------------------------------------------------------------------------------  




# ------------------------------------------ Delete Product -------------------------------------------------------------------------
def del_product(request,pk):
    product = Product.objects.get(pk=pk)
    context = {
        'product':product,
    }
    if request.method=='POST':
        product.delete()

        return redirect('/myapp/product')

    return render(request, 'myapp/delete.html', context)
# ---------------------------------------------------------------------------------------------------------------------  





# ------------------------------------------ List all products -------------------------------------------------------------------------
def my_listings(request):
    products = Product.objects.filter(seller_name=request.user)
    context = {
        'products':products
    }
    
    return render(request, 'myapp/my_listings.html', context)
# ---------------------------------------------------------------------------------------------------------------------     