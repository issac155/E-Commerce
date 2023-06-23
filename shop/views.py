from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from .models import cat, Product
from .models import Comment
from datetime import datetime,date
from django.http.response import JsonResponse
from django.db.models.query_utils import Q


 
def index(request):
 
  ca = cat.objects.all()
  o = Product.objects.order_by('date')[:8]
  if 'fi' in request.COOKIES:
    ui = request.COOKIES['fi']
    ki = request.COOKIES['oi']
    print(ui,ki)
  return render(request,'index.html',{'ca':ca, 'o':o})

def contact(request):
  return render(request,'contact.html')

def detail(request):
  return render(request,'detail.html')

def login1(request):
  if request.method == "POST":
    a = request.POST['username']
    b = request.POST['password']
   
    user = auth.authenticate(username=a,password=b)
    

    if user is not None:
      auth.login(request,user)

      si = redirect("/")
      first = User.objects.get(username = a)
      second = User.objects.get(username = a)
      si.set_cookie('fi',first.first_name)
      si.set_cookie('ji',second.last_name)
      si.set_cookie('oi',first.email)
      
      si.set_cookie("valid",True)
      return si
    else:
      c= "Invalid username or password"
      return render(request, 'Log in.html',{'msg':c})
  else:
    return render(request, 'Log in.html')

def req(request):
   if request.method == 'POST':
       a = request.POST['firstname']
       b = request.POST['lastname']
       c = request.POST['username']
       d = request.POST['email']
       e = request.POST['password']
       f = request.POST['repassword']
       
       if c != ''  and  d != ''  and  e != '' :
        
        if e == f :
        
          if User.objects.filter(username = c).exists() or User.objects.filter(email = d).exists():
            z = "User already found"
            return render(request, 'Register.html',{'msg':z})
          else:
            hello = User.objects.create_user(first_name = a, last_name = b, username = c, email = d, password = e)
            hello.save()
            auth.login(request,hello)
            return redirect('/')
        else:
          k = "Password Miss Match"
          return render(request, 'Register.html',{'msg':k})

       else:
        h = "Required Field is Empty"
        return render(request, 'Register.html',{'msg':h})

   else:
    return render(request, 'Register.html')

def logout(request):
  auth.logout(request)
  yi = redirect("/")
  yi.delete_cookie('fi')
  yi.delete_cookie('ji')
  yi.delete_cookie('oi')
  yi.delete_cookie('valid')
  return yi
 

def cat1(request):
  a = request.GET['ab']
  b = Product.objects.filter(ship = a)
  return render(request,'shop.html',{'b':b})

def pro1(request):

 
  
  if request.user.is_authenticated:
    c = request.GET['bc']
    d = Product.objects.get(id=c)
    if 'absection' in request.session:
      if c in request.session['absection']:
        request.session['absection'].remove(c)
      yi = Product.objects.filter(id__in=request.session['absection'])
      print("hello")
      print(c)
      request.session['absection'].insert(0,c)
      if len(request.session['absection']) > 3:
        request.session['absection'].pop()
    else:
      request.session['absection']=[c]
      yi = Product.objects.filter(id = c)
    
    request.session.modified = True
    print(yi)
    return render(request, 'detail.html',{'d':d,'yi':yi} )
  else:
    return render(request, 'Log in.html')

def invo(request):
  e = request.POST['no']
  f = request.POST['io']
  g = Product.objects.get(id=f)
  h = g.price*int(e)
  print(h)
  print(f)
  
  
  k = datetime.now()
  # k = datetime.now
  # l = k.strftime("%I:%M %p")
  
  return render(request,'invoice.html' ,{'g':g, 'h':h,'e':e ,'k':k} )

def bro1(request):
 
 if request.user.is_authenticated:
  c = request.GET['ic']
  d = Product.objects.get(id=c)
  if 'absection' in request.session:
      if c in request.session['absection']:
        request.session['absection'].remove(c)
      yi = Product.objects.filter(id__in=request.session['absection'])
      print("hello")
      print(c)
      request.session['absection'].insert(0,c)
      if len(request.session['absection']) > 3:
        request.session['absection'].pop()
      else:
       request.session['absection']=[c]
      yi = Product.objects.filter(id = c)
    
      request.session.modified = True
      print(yi)

      return render(request, 'detail.html',{'d':d ,'yi':yi})
 else:
    return render(request, 'Log in.html') 

def add(request):
   a = request.GET['ty']
   b = request.GET['ji']
   c = request.GET['si']
   print(a,b,c)
   user = User.objects.get(id=b)
   k = Comment.objects.create(u_name=user.username,u_body=a,product_id=c)
   k.save()
   return redirect('/cat/pro/?bc='+c)
  

def search1(request):
  if 'term' in request.GET:
    h = request.GET['term']
    print(h)
    l = Product.objects.filter(Q(name__istartswith=h))
    dot = []
    for i in l:
      dot.append(i.name)
    return JsonResponse(dot,safe = False)
  return redirect('/')

def search2(request):
  k = request.POST['ser']
  if Product.objects.filter(name=k):
    d = Product.objects.get(name=k)
    print(d)
    return render(request, 'detail.html',{'d':d})
  else:
      z = "Product not found "
      return render(request, 'detail.html',{'msg':z})



  

