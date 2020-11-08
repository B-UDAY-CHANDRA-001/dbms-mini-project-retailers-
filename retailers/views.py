from django.shortcuts import render, redirect
from retailers.forms import ItemsForm, CustomersForm, CartForm, CartDetailsForm,OrderDetailsForm
from retailers.models import Items, Customers, Cart, Cart_contains, Orders
from django.db import connection
from django.contrib import messages


def home(request):
    items = Items.objects.all()
    return render(request, 'home.html', {'items': items})
def developer(request):
    return render(request, 'developer.html',)

def std(request):
    if request.method == "POST":
        form = ItemsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect('/items')
            except:
                pass
    else:
        form = ItemsForm()
    return render(request, 'add_items.html', {'form': form})


def items(request):
    items = Items.objects.all()
    return render(request, "products.html", {'items': items})


def cust(request):
    if request.method == "POST":
        form = CustomersForm(request.POST)
        if form.is_valid():
            try:
                form.save()

                return redirect('/customers')
            except:

                pass
    else:
        form = CustomersForm()
    return render(request, 'add_customers.html', {'form': form})


def customers(request):
    customers = Customers.objects.all()
    return render(request, "customers.html", {'customers': customers})

def delete_cust(request,id):
    customer = Customers.objects.get(id=id)
    customer.delete()
    return redirect('/customers')


def cart(request):
    if request.method == "POST":
        form = CartForm(request.POST)
        if form.is_valid():
            try:
                form.save()

            except:
                pass
    else:
        form = CartForm()
    cart = Cart.objects.all()
    return render(request, 'cart.html', {'form':form, 'cart': cart})


def delete_cart(request, id):
    carts = Cart.objects.get(id=id)
    carts.delete()
    return redirect("/cart")

def update_cart(request, id):
    context = {}
    obj = Cart.objects.get(id=id)
    form = CartForm(request.POST,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/cart')
    context["form"] = form
    return render(request, "update_cart.html", context)
def cart_contains(request):
    if request.method == "POST":
        if request.POST.get('Customer_id') and request.POST.get('Order_id') and request.POST.get('Product_id')and \
                request.POST.get('Quantity')and request.POST.get('Price')and request.POST.get('Date')and \
                request.POST.get('Order_status'):
            saverec = Cart_contains()
            saverec.Customer_id = request.POST.get('Customer_id')
            saverec.Order_id = request.POST.get('Order_id')
            saverec.Product_id = request.POST.get('Product_id')
            saverec.Quantity = request.POST.get('Quantity')
            saverec.Price = request.POST.get('Price')
            saverec.Date = request.POST.get('Date')
            saverec.Order_status = request.POST.get('Order_status')
            cursor = connection.cursor()
            cursor.execute("call `cart-split`('"+saverec.Customer_id+"','"+saverec.Order_id+"','"+saverec.Product_id+"','"+saverec.Quantity+"','"+saverec.Price+"','"+saverec.Date+"','"+saverec.Order_status+"')")
            messages.success(request,"Added Customer  "+saverec.Customer_id+" Sucessfully!!")
            return render(request, "cart_contains.html")
    else:
        return render(request, "cart_contains.html")


def order_details(request):
    resultdisplay = Orders.objects.all()
    return render(request,'order_details.html',{'Orders':resultdisplay})


