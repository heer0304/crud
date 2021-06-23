from django.shortcuts import render
from .forms import OrderForm
from .models import Product
# Create your views here.

def createOrder(request):
    if request.method == 'POST':
        form = OrderForm()
        products = Product.objects.get(id=product_id)
        if form.is_valid():
            form.save()
        return render(request, 'orderForm.html',{'form':form})
    else:
        form = OrderForm
        return render(request, 'orderForm.html',{'form':form})

def updateView(request):
    return render(request, 'updateView.html')

def deleteView(request):
    pass