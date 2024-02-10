from django.shortcuts import render

# Create your views here.

def filters(request):
    data = "Meirda tech minds"

    return render(request,'filters.html',{'data':data})
    


