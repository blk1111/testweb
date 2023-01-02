from ..models import sp
from django.shortcuts import render

def update_(request,pid):
    plist = sp.objects.get(id=pid)
    if request.method == "POST":
        plist.name = request.POST['name']
        plist.price = request.POST['pic']
        plist.png = request.POST['png']
        plist.save()      
          
        splist = sp.objects.all()
        context = {'splist' : splist}
        return render(request,'login.html',context) 
    context = {'plist' : plist}
    return render(request,'update.html',context)
