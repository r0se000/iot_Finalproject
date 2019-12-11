from django.shortcuts import render, redirect
from .models import Datain

# Create your views here.
def search(request):
    return render(request, 'search.html')

# 예외처리 x 실행 o
# def home(request):
#     id=request.GET.get('id', ' ')
#     if id:
#         f=Values.objects.filter(mid=id)
#         reverse=f.order_by('-time')
#         data=reverse[:1]
#         return render(request, 'home.html', {'data' : data})

# 예외처리
def home(request):
    n=request.GET.get('n', ' ')
    f=Datain.objects.filter(mid=n)
    reverse=f.order_by('-time')
    data=reverse[:1]
    if data:    
        return render(request, 'home.html', {'data' : data})
    else :
        return redirect('search')
