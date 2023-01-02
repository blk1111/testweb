from django.urls import path,include
from . import views
from .allDate import del_,insert_,update_

urlpatterns = [
    path('', views.index,name='Index'),
    path('login/',views.login,name='Login'),
    path('update/<str:pid>', update_.update_, name='update'),
    path('del/<str:pid>', del_.del_, name='del'),
    path('splist/',views.splist,name='splist'),
    path('insert/<str:pid>', insert_.insert_, name='Insert'),
]