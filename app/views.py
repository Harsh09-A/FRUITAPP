from django.shortcuts import render
from django.contrib.auth import authenticate
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import logout as log_out
from django.contrib.auth import login as as_login
from app.models import Products
from app.models import Addtocart
from app.models import Wishlist
from app.models import Query
from django.contrib.auth.hashers import make_password
from django.db.models import Sum
# Create your views here.
def index(request):
    prodname = Products.objects.all()
    wish = Wishlist.objects.all().count()
    cart = Addtocart.objects.all().count()
    request.session['wishcount'] =wish
    request.session['cartcount'] =cart
    x={'prodname':prodname,}
    return render(request, 'pages/index.html', {'x':x})

def shop(request):
    return render(request, 'pages/shop.html')

# ..............single product page................
def product(request,id):
    obj = Products.objects.get(pk=id)
    return render(request, 'pages/product.html',{'prod':obj})

# ..............end single product page..............

def login(request):
    return render(request, 'pages/login.html')

def register(request):
    return render(request, 'pages/register.html')

def contact(request):
    return render(request, 'pages/contact.html')

def checkout(request):
    cart2 = Addtocart.objects.all()
    cartprice = Addtocart.objects.aggregate(Sum('Product_Discount_price'))
    cartprice=cartprice.get('Product_Discount_price__sum')
    totalgd=cartprice+40
    x={'cartprice':cartprice,'cart':cart2,'total':totalgd}
    return render(request, 'pages/checkout.html', {'x':x})

def cart(request):
    cart = Addtocart.objects.all()
    wish = Wishlist.objects.all().count()
    cart2 = Addtocart.objects.all().count()
    cartprice = Addtocart.objects.aggregate(Sum('Product_Discount_price'))
    cartprice=cartprice.get('Product_Discount_price__sum')
    totalgd=cartprice+40
    x={'cartprice':cartprice,'cart':cart,'total':totalgd}
    request.session['wishcount'] =wish
    request.session['cartcount'] =cart2
    return render(request, 'pages/cart.html',{'cart':x})

def wishlist(request):
    wish = Wishlist.objects.all()
    wish2 = Wishlist.objects.all().count()
    cart = Addtocart.objects.all().count()
    request.session['wishcount'] =wish2
    request.session['cartcount'] =cart
    return render(request, 'pages/wishlist.html', {'wish':wish})

def myacc(request):
    return render(request, 'pages/myaccount.html')
# ..............add to cart............................
def addcard(request,id):
    obj = Products.objects.get(pk=id)
    if Addtocart.objects.filter(Product_id=id).exists() :
        messages.success(request, 'Product Already Added in your Card!')
        return redirect('/')
    else:
        Product_id=obj.id
        Product_name=obj.Product_name
        Product_Price=obj.Product_Price
        Product_Discount_price=obj.Product_Discount_price
        Product_Unit=obj.Product_Unit
        Product_img=obj.Product_img
        reg=Addtocart(Product_id=Product_id,Product_name=Product_name,Product_Price=Product_Price,Product_Discount_price=Product_Discount_price,Product_Unit=Product_Unit,Product_img=Product_img,)
        reg.save()
        messages.success(request, 'Product Succesfully Add in your Card!')
        return redirect('/')
# ...................end add to cart.................................
# ...................whislist start.................................
def whishlist2(request,id):
    obj = Products.objects.get(pk=id)
    if Wishlist.objects.filter(Product_id=id).exists() :
        messages.success(request, 'Product Already Added in your Whislist!')
        return redirect('/')
    else:
        Product_id=obj.id
        Product_name=obj.Product_name
        Product_Price=obj.Product_Price
        Product_Discount_price=obj.Product_Discount_price
        Product_Unit=obj.Product_Unit
        Product_img=obj.Product_img
        reg=Wishlist(Product_id=Product_id,Product_name=Product_name,Product_Price=Product_Price,Product_Discount_price=Product_Discount_price,Product_Unit=Product_Unit,Product_img=Product_img,)
        reg.save()
        messages.success(request, 'Product Succesfully Add in your Whislist!')
        return redirect('/')
# ...................end wishlist...................................
#                    registration
def regdata(request):
    try:
        username = request.POST['username']
        email = request.POST['email']
        first_name = request.POST['fname']
        last_name = request.POST['lname']
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        if (password==cpassword):
            password2=make_password(password)
            reg=User(username=username,email=email,first_name=first_name,last_name=last_name,password=password2,)
            reg.save()
            messages.success(request, 'Thank You For Contact us!')
            return redirect('register')
        else:
            messages.error(request, 'Password and confirm password does not matched!')
            return redirect('register')
    except:
        messages.error(request, 'Please Try Again Something is Wrong')
        return redirect('register')
#                    end resitration
# ................delet add to cartd products.......................
def adddel(request,id):
    Addtocart.objects.filter(Product_id=id).delete()
    return redirect('cart')
# ................delet end edd  to card..................................
# ................delet wishlist products.......................
def wishdel(request,id):
    Wishlist.objects.filter(Product_id=id).delete()
    return redirect('wishlist')
# ................end wishlist products..................................
#  .................login.................
def userlogin(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        as_login(request, user)
        messages.success(request, 'Welcome to Fruit Shop !')
        return redirect('/')
    else:
        messages.error(request, 'Please Fill User Name And Password')
        return redirect('login')
# ...................logout.......................
def logout(request):
    log_out(request)
    return redirect('home')

# ................query...................
def query(request):
    qname = request.POST['qname']
    qemail = request.POST['qemail']
    qphone = request.POST['qphone']
    qcity = request.POST['qcity']
    qsubject = request.POST['qsubject']
    qmessage = request.POST['qmessage']
    reg=Query(name=qname,email=qemail,phone=qphone,city=qcity,subject=qsubject,qmessage=qmessage,)
    reg.save()
    messages.success(request, 'Thank You For Contact Us !')
    return redirect('home')