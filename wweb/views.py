from django.shortcuts import render,redirect

from .models import sp,ssp

from .allDate import spLoad

# Create your views here.
def index(request):#首頁(非登入)
    splist = sp.objects.all()
    content = {'splist' : splist}  
    return render(request,'index.html',content)

def login(request):
    splist = sp.objects.all()
    content = {'splist' : splist}
    user = request.POST.get('user','')
    pwd = request.POST.get('pwd','')
    if(user is not None and pwd is not None and user == 'test' and pwd == 'user'):    
        return render(request,'login.html',content)
    else:
        return redirect('/')   

def splist(request):
    if request.method == "POST":
        splist = ssp.objects.all()
        splist.delete()
        
        splist = sp.objects.all()
        context = {'splist' : splist}
        return render(request,'login.html',context)  
    context = {'ssplist':spLoad.sp_(request.GET['name'],request.GET['page'])}
    return render(request,'splist.html',context)


        





