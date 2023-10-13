from django.shortcuts import render
from Shop.models import Product
from django.db.models import Q
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def Searchresult(request):
    query=""
    product=None
    if(request.method=="POST"):
        query=request.POST['q']
        if query:
            product=Product.objects.filter(Q(pname__icontains=query) | Q(description__icontains=query))
    return render(request,'Search.html',{'p':product,'q':query})
