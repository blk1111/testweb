from django.shortcuts import render,redirect
from ..models import sp,ssp

def insert_(request,pid):
    ssplist = ssp.objects.get(id=pid)
    if request.method == "POST":    
        insertList = sp.objects.create(name=ssplist.sname,png=ssplist.spng,price=ssplist.spic)
        insertList.save()
        ssplist = ssp.objects.all()
        context = {'ssplist' : ssplist}
        return render(request,'splist.html',context)
    context = {'ssplist':ssplist}    
    return render(request,'insert.html',context)
