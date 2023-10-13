from django.shortcuts import render,redirect
from Cart.models import Cart,Account,Order
from Shop.models import Product
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Add_to_cart(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart = Cart.objects.get(user=user,product=product)
        if(cart.quantity<cart.product.stock):
            cart.quantity+=1
        cart.save()
    except Cart.DoesNotExist:
        cart=Cart.objects.create(product=product, user=user,quantity=1)
        cart.save()
    return redirect('Cart:Cart_view')
@login_required
def Cart_view(request):
    Total=0
    user=request.user


    cart=Cart.objects.filter(user=user)
    for i in cart:
        Total+=i.quantity * i.product.price
    return render(request,'Cart.html',{'cart':cart,'Total':Total})
@login_required
def Cart_remove(request,p):
    product=Product.objects.get(pname=p)
    user=request.user
    try:
        cart=Cart.objects.get(user=user,product=product)
        if(cart.quantity>1):
            cart.quantity-=1
            cart.save()

        else:cart.delete()
    except:
        pass
    return redirect('Cart:Cart_view')
@login_required
def Full_remove(request,p):
    product = Product.objects.get(pname=p)
    user = request.user
    try:
        cart = Cart.objects.get(user=user, product=product)
        cart.delete()

    except:
        pass
    return redirect('Cart:Cart_view')



# def Check_out(request):
#     total=0
#     user=request.user
#     cart=Cart.objects.filter(user=user)
#     for i in cart:
#         total+=i.quantity * i.product.price
#     return render(request,'Cart.html',{'Cart':Cart,'Total':total})

@login_required

def Order_form(request):
    if(request.method=="POST"):
        a=request.POST['Add']
        p=request.POST['Pho']
        ac=request.POST['Acc']
        user=request.user
        cart=Cart.objects.filter(user=user)
        total=0
        for i in cart:
            total=i.quantity*i.product.price


        account=Account.objects.get(AccountNumber=ac)
        if(account.balance>total):
            account.balance=account.balance-total
            account.save()
            for i in cart:
                o=Order.objects.create(user=user, product=i.product, phone=p, place=a, noofitems=i.quantity, order_status="Paid")
                o.save()
                i.product.stock=i.product.stock-i.quantity
                i.product.save()
            cart.delete()
            msgs="Order Placed successfully"
            return render(request,'Order confirm.html',{'msg':msgs})
        else:
            msg="Insufficient Amount.You Can't Place order"
            return render(request,'Order confirm.html',{'msg':msg})
    return render(request,'Order Form.html')



def Orders(request):
    user=request.user
    s=Order.objects.filter(user=user)
    return render(request,'Orders.html',{'s':s,'u':user.username})