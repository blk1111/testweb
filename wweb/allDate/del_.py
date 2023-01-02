from ..models import sp
from django.shortcuts import render

def del_(request,pid):
    dlist = sp.objects.get(id=pid)  
    if request.method == "POST":
       
        dlist.delete()

        splist = sp.objects.all()
        context = {'splist' : splist}
        return render(request,'login.html',context)
    
    context = {'dlist' : dlist}

    return render(request, 'del.html', context)