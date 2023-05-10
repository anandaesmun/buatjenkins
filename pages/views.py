from django.shortcuts import render

# Create your views here.
def home(request):
    if request.method == 'POST':
        a = request.POST['a']
        b = request.POST['b']
        if 'add' in request.POST:
            result = tambah(a,b)
            return render(request,'index.html',{'result':result})
    return render(request,'index.html')

# functions
def tambah(a, b):
    return int(a) + int(b)
