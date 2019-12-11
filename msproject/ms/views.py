from django.shortcuts import render, redirect
from .models import Datain

# Create your views here.
def search(request):
    return render(request, 'search.html')

def home(request):
    n=request.GET.get('n', ' ')
    f=Datain.objects.filter(mid=n)
    reverse=f.order_by('-time')
    data=reverse[:1]
    if data:    
        return render(request, 'home.html', {'data' : data})
    else :
        return redirect('search')
