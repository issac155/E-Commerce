from django.urls import path
from . import views
from django.conf import settings 
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('log/', views.login1, name='log'),
    path('req',views.req,name='re'),
    path('contact', views.contact, name='contact'),
    path('detail',views.detail, name='detail'),
    path('out',views.logout, name='out'),
    path('cat/',views.cat1,name='cat'),
    path('cat/pro/', views.pro1,name = 'pro'),
    path('fe', views.invo,name='fe'),
    path('bro/' ,views.bro1, name='bro'),
    path('hi/' , views.add, name='hi'),
    path('search/', views.search1, name='ser'),
    path('search4/',views.search2,name='search4')
    

]


urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root= settings.MEDIA_ROOT)