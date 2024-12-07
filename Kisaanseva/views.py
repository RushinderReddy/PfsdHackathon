import datetime
import users
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from .models import *


def index(request):
    return render(request, 'home.html')
def registers(request):
    register=False
    if request.method == 'POST':
        name=request.POST.get('name')
        uname = request.POST.get('email')
        pwd = request.POST.get('pd')
        cp=request.POST.get('cpd')
        if User_module.objects.filter(email=uname).count() > 0:
            return render(request, 'login.html', {'error': 'Email already Exist'})
        else:
            user = User_module(username=name,email=uname, password=pwd,cpassword=cp)
            user.save()
            subject='Thanks For Registering'
            message='HEY '+user.username+''+',you are now successfully registered with KisaanSeva.You’ve taken the first step toward becoming a part of our website. We’ll send you timely email and text reminders of new orders through email. We are overwhelmed with your registration.'
            to=user.email
            send_mail(
                subject,
                message,
                'kalyan27@gmail.com',
                [to],
            )
            register=True
        return redirect('/login')
    else:
        return render(request, 'login.html',{'msg':'enter valid details'})
    return users

def login(request):
    return render(request,'login.html')
def loginuser(request):
    print(0.1)
    # request.session['cartitems'] = []
    if request.method == 'POST':
        print(0.2)
        uname = request.POST.get('name')
        pwd = request.POST.get('lpd')
        check_user = User_module.objects.filter(username=uname, password=pwd)
        request.session.modifed = True
        if uname == "Kisaanseva" and pwd == "admin":
            return render(request,'admin.html')
        if check_user:
            print(0.3)
            #member = User.objects.get(email=request.POST['login_email'], password=request.POST['lpd'])
            #email=User.objects.get(email=request.POST['login_email'])
            #request.session['email'] = email
            request.session['user'] = uname

            #request.session['cartorder'] = "kishan"
            return render(request, 'index.html',{"username":uname})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'home.html', context)
        return user
def fp(request):
    return render(request,'fp.html')
def forget_pwd(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        pwd = request.POST.get('lpd')
        check_user = Users.objects.get(username=uname)
        if check_user:
            check_user.password=pwd
            check_user.save()
        return render(request,'login.html',{'msg':'Password Updated'})
def menu(request):
    uname=request.session['user']
    return render(request,'menu.html',{'name':uname})
def userinfo(request):
    student=User_module.objects.all()
    return render(request, 'display.html', {'student':student,'title':'User Info'})


from django.shortcuts import render
from .models import Item  # Assuming the model name is Item


from django.shortcuts import render
from .models import Item

from django.shortcuts import render
from .models import Item

from django.shortcuts import render, redirect
from .models import Item
  # Assuming you have a Cart class to manage cart operations


def fsd(request):
    fsditems = items.objects.filter(category="Fertilizer Spraying Drones")
    return render(request, 'fsd.html', {'fsditems': fsditems})


def wsd(request):
    wsditems = items.objects.filter(category="Water Spraying Drones")
    return render(request, 'wsd.html', {'wsditems': wsditems})
def std(request):
    stdtems = items.objects.filter(category="Soil Testing Drones")
    return render(request, 'std.html', {'stdtems': stdtems})

def sfcd(request):
    sfcditems = items.objects.filter(category="Security Drones")
    return render(request, 'sfcd.html', {'sfcditems': sfcditems})
def dd(request):
    dditems = items.objects.filter(category="Deserts & Drinks")
    return render(request, 'dd.html',{'dditems': dditems})
def ss(request):
    ssitems = items.objects.filter(category="Snacks & Starters")
    return render(request, 'ss.html',{'ssitems': ssitems})
def sp(request):
    spitems = items.objects.filter(category="Seasonal Specials")
    return render(request, 'sp.html',{'spitems': spitems})


from django.shortcuts import render, redirect, get_object_or_404
from .models import User, storeItem, items  # Adjust imports based on your actual model names
from django.db.models import Sum


def get_cart_items(request):
    # Check if user is logged in
    if 'user' not in request.session:
        return redirect('login')  # Redirect to login if user is not authenticated

    uname = request.session['user']

    try:
        user = User.objects.get(username=uname)  # Replace 'users' with 'User'
    except User.DoesNotExist:
        return render(request, 'error.html', {'message': 'User does not exist.'})

    # Get all cart items for the user
    cart_items = StoreItem.objects.filter(users=user)

    # Calculate total amount
    total_amount = sum(cart_item.quantity * cart_item.items.price for cart_item in cart_items)

    # Prepare context for rendering
    context = {
        'cart_items': cart_items,
        'total': total_amount,
    }

    return render(request, 'cart.html', context)


def ws(request):
    wsitems = Items.objects.filter(category="Weekend Specials")  # Adjust based on your model names
    return render(request, 'ws.html', {'wsitems': wsitems})


def goback(request):
    name = request.session.get('user', '')  # Use get to avoid KeyError if 'user' is not present
    return render(request, 'index.html', {'username': name})
def thankyou(request):
    return render(request, 'login.html')


def logout(request):
    del request.session['user']
    return redirect('/login')
def productinfo(request):
    pro = items.objects.all()
    return render(request, 'displayproduct.html', {'pro':pro,'title':'ProductDetails Info'})
def additem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category=request.POST.get('category')
        image=request.POST.get('image')
        items= items(name=name, price=price,category=category,image=image)
        items.save()
        return render(request,'additem.html',{'msg': 'Added'})
    else:
        return render(request, 'admin.html')
def add(request):
    return render(request,'additem.html')
def delete(request):
    pro = items.objects.all()
    return render(request, 'delete.html', {'pro': pro, 'title': 'ProductDetails Info'})
def deleteitem(request,name):
    pro = items.objects.get(name = name).delete()
    return render(request, 'admin.html', {'msg': 'Deleted'})
def update_form(request,name,price):
    return  render(request,'updateitem.html',{'name':name,'price':price})
def updateitem(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        price = request.POST.get('price')
        category=request.POST.get('category')
        pro = item.objects.get(name=name)
        pro.name=name
        pro.category=category
        pro.price=price
        pro.save()
        return render(request, 'admin.html', {'msg': 'updated'})
    else:
        return render(request, 'admin.html', {'msg': 'cannotupdate'})
def update(request):
    pro = items.objects.all()
    return render(request, 'update.html', {'pro':pro,'title':'ProductDetails Info'})


from django.shortcuts import redirect, get_object_or_404
 # Ensure you have the correct imports


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import storeItem, CartItem  # Assuming CartItem is your cart model
from django.contrib import messages

@login_required
def cart_add(request, name):
    # Ensure the user is logged in (this is handled by the @login_required decorator)
    if request.method == 'POST':
        try:
            # Get the logged-in user
            user = request.user

            # Get the item by its name (assuming 'name' is unique)
            item = storeItem.objects.get(name=name)

            # Get the quantity from the form submission (default to 1)
            quantity = int(request.POST.get('qty', 1))

            # Check if the item already exists in the user's cart
            cart_item, created = CartItem.objects.get_or_create(user=user, item=item)

            if created:
                cart_item.quantity = quantity  # If it's a new item in the cart, set the quantity
            else:
                cart_item.quantity += quantity  # If item already exists, increase the quantity

            cart_item.save()

            # Success message
            messages.success(request, f'{item.name} has been added to your cart.')

        except storeItem.DoesNotExist:
            messages.error(request, f'{name} does not exist in the store.')
        except Exception as e:
            messages.error(request, f'An error occurred: {e}')

        return redirect('cart')  # Redirect to cart view or another page

    return redirect('store')  # In case of incorrect request method (GET), redirect back to the store

    cartitems = storeItem.objects.filter(items__name = name)
    cartitems.delete()
    return redirect(request.META['HTTP_REFERER'])
def cart_view(request):
    # Fetch cart items and calculate total price
    return render(request, 'cart.html', {'cart_items': cart_items, 'total': total_amount})

def order(request):
    return render(request,'order.html')
def cart(request):
    return render(request,'cart.html')
def end(request):
    return render(request,'end.html')



def amount(request,total,cart_items):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    cart_items = storeItem.objects.filter(users=user).first()
    order=orders_food.objects.create(
        cart_items=cart_items,
        total=total
    )
    return render(request,'amount.html')
def pay(request):
    return render(request,'payment.html')
def addpayment(request):
    if request.method == 'POST':
        name = request.POST.get('firstname')
        email = request.POST.get('email')
        address=request.POST.get('address')
        city=request.POST.get('city')
        zip = request.POST.get('zip')
        state = request.POST.get('state')
        name_on_card = request.POST.get('cardname')
        cardno = request.POST.get('cardnumber')
        expmonth = request.POST.get('expmonth')
        expyear = request.POST.get('expyear')
        cvv = request.POST.get('cvv')
        payments = bills(name=name, email=email,address=address,city=city,zip=zip,state=state,name_on_card=name_on_card,cardno=cardno,expmonth=expmonth,expyear=expyear,cvv=cvv)
        payments.save()
        return render(request,'end.html')
def contact(request):
    return render(request,'contact.html')
def about(request):
    return render(request,'about.html')
@login_required(login_url='/loginusers')
def table(request):
    date_table=datetime.date.today()
    time_table=datetime.datetime.now().time()
    bcount=1
    a = book_table.objects.filter(date_table=date_table).count()
    b = bcount - a
    if b==0:
        print("all tables booked")
    return render(request,'table.html',{'tcount':b})
def add_table(request):
    date_table = datetime.date.today()
    time_table = datetime.datetime.now().time()
    bcount = 1
    a = book_table.objects.filter(date_table=date_table).count()
    b = bcount - a
    if b>0:
        if request.method=='POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            date_table = request.POST.get('date')
            time_table = request.POST.get('time')
            category = request.POST.get('category')
            msg = request.POST.get('guest')
            book=book_table(name=name,email=email,phone=phone,date_table=date_table,time_table=time_table,category=category,guest=msg)
            book.save()
            return render(request,'end.html',{'msg':'Table Booked Sucessfully'})
    else:
        return render(request, 'sorry.html', {'msg': 'Total Table Booked'})
def feedback(request):
    return render(request,'feedback.html')
def cater(request):
    uname = request.session['user']
    return render(request,'order.html',{'username':uname})
from django.shortcuts import render
from .models import Fertilizer  # Replace with your actual model name

def fertilizer_list(request):
    ritem = Fertilizer.objects.all()  # Query all fertilizers
    context = {'ritem': ritem}  # Pass to the template
    return render(request, 'fertilizer_list.html', context)  # Template name matches your HTML file

def desserts(request):
    return render(request, 'desserts.html')
def tropics(request):
    return render(request, 'tropics.html')
def maincourse(request):
    return render(request, 'main.html')
def paan(request):
    return render(request, 'paan.html')
def relishes(request):
    return render(request, 'relishes.html')
def cart_add_fertilizers(request,name):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    items = get_object_or_404(ritem,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItem.quantity = qty
        cart_item = storeItem.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )

def dishes(request):
    return render(request, 'dishes.html')
def drinks(request):
    return render(request, 'drinks.html')
def delights_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    if request.method=="POST":
        dcategory = request.POST.get('dcategory')
        dcapacity=request.POST.get('dcapacity')
        items=item.objects.get(name=dcategory)
        dprice=items.price*int(dcapacity)
        delight = Query_table(uname=user.username,dcategory=dcategory,dcapacity=dcapacity,dprice=dprice)
        delight.save()
        print(str(delight.cid))
        return render(request,'catering.html',{'msg':'Delights added to menu'})
def desserts_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    cater_order= Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method=="POST":
        dcategory = request.POST.get('decategory')
        decapcity=request.POST.get('decapcity')
        items = item.objects.get(name=dcategory)
        deprice = items.price * int(decapcity)
        cater_order.decategory=dcategory
        cater_order.decapacity=decapcity
        cater_order.deprice=deprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Desserts added to menu'})
def dishes_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    cater_order = Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        dicategory = request.POST.get('dicategory')
        dicapcity = request.POST.get('dicapcity')
        items = item.objects.get(name=dicategory)
        deprice = items.price * int(dicapcity)
        cater_order.dicategory = dicategory
        cater_order.dicapacity = dicapcity
        cater_order.diprice=deprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Dishes added to menu'})
def paan_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        pcategory = request.POST.get('pcategory')
        pcapcity = request.POST.get('pcapcity')
        items = item.objects.get(name=pcategory)
        pprice = items.price * int(pcapcity)
        cater_order.pcategory = pcategory
        cater_order.pcapacity = pcapcity
        cater_order.pprice=pprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Paan Specials added to menu'})
def tropics_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order =Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('tcategory')
        tcapcity = request.POST.get('tcapacity')
        items = item.objects.get(name=tcategory)
        tprice = items.price * int(tcapcity)
        cater_order.tcategory = tcategory
        cater_order.tcapacity = tcapcity
        cater_order.tprice=tprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Tropics added to menu'})
def drinks_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('drcategory')
        tcapcity = request.POST.get('drcapcity')
        items = item.objects.get(name=tcategory)
        drprice = items.price * int(tcapcity)
        cater_order.drcategory = tcategory
        cater_order.drcapacity = tcapcity
        cater_order.drprice=drprice
        cater_order.save()
        return render(request,'catering.html',{'msg':'Drinks added to menu'})
def relishes_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('recategory')
        tcapcity = request.POST.get('recapacity')
        item = items.objects.get(name=tcategory)
        rprice = items.price * int(tcapcity)
        cater_order.rcategory = tcategory
        cater_order.rcapacity = tcapcity
        cater_order.rprice=rprice
        cater_order.save()
        return render(request, 'catering.html', {'msg': 'Relishes added to menu'})
def maincourse_add(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Query_table.objects.get(uname=user.username)
    print(str(cater_order))
    if request.method == "POST":
        tcategory = request.POST.get('maincategory')
        tcapcity = request.POST.get('maincapcity')
        item = items.objects.get(name=tcategory)
        mprice = items.price * int(tcapcity)
        cater_order.maincategory = tcategory
        cater_order.maincapacity = tcapcity
        cater_order.mprice=mprice
        cater_order.save()
        return render(request, 'catering.html', {'msg': 'Main Course added to menu'})
def get_cater_items(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order = Query_table.objects.get(uname=user.username)
    if cater_order:
        t=int(cater_order.dprice)+int(cater_order.diprice)+int(cater_order.deprice)+int(cater_order.drprice)+int(cater_order.pprice)+int(cater_order.tprice)+int(cater_order.mprice)+int(cater_order.rprice)
        context={
            'cater':cater_order,
            'total':t,
            }
        return render(request,'order.html',context)
    else:
        return render(request, 'order.html', {'msg':'Menu NOt Selected!!!!!'})

def cater_order(request):
    return render(request,'end.html')
def feedback_add(request):
    if request.method=='POST':
        firstname=request.POST.get('firstname')
        mailid=request.POST.get('mailid')
        service=request.POST.get('service')
        food=request.POST.get('food')
        cleanliness=request.POST.get('cleanliness')
        ResponseTime=request.POST.get('Response Time')
        recommend=request.POST.get('recommend')
        rating=request.POST.get('rating')
        fb = Feedback_form(firstname=firstname,mailid=mailid,service=service,food=food,cleanliness=cleanliness,ResponseTime=ResponseTime,recommend=recommend,rating=rating)
        fb.save()
        return render(request,'feedback.html',{'msg':'Review Submited'})
def add_contact(request):
    if request.method=='POST':
        name=request.POST.get('name')
        email = request.POST.get('email')
        city = request.POST.get('city')
        query = request.POST.get('query')
        c=Contact_details(name=name,email=email,city=city,query=query)
        c.save()
        return render(request, 'contact.html', {'msg': 'Query Submited To Team'})
def pre_order(request):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    # cid=request.session['cid']
    cater_order =orders_foods.objects.all()
    return render(request, 'history.html', {'history': cater_order})
def pay_page(request):
    return render(request,'amount.html')
def search_add(request):
    if request.method=='POST':
        search = request.POST.get('search')
        item=items.objects.filter(name=search)
        return render(request,'search.html',{'items':items})
def cart_add_search(request,name):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    item = get_object_or_404(items,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItem.quantity = qty
        cart_item = storeItem.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )

    return render(request,'menu.html',{'msg':'Added To Cart'})
def dummy(request):
    i=items.objects.all()
    return render(request,'dummy.html',{'items':i})
def add_rec(request):
    if request.method=='POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        age = request.POST.get('age')
        taste = request.POST.get('taste')
        timing = request.POST.get('timing')
        new = request.POST.get('new')
        rec=recommendations(name=name,email=email,age=age,phone=phone,kind=taste,time=timing,newvar=new)
        rec.save()
        if rec.time=="morning":
            return render(request, 'morning.html')

        elif rec.time=="afternoon":
            ra = ritem.objects.filter(category="afternoon")
            return render(request, 'after.html',{'ra':ra})
        elif rec.time=="evening":
            re = ritem.objects.filter(category="evening")
            return render(request, 'eve.html',{'re':re})
        elif rec.time=="night":
            rn= ritem.objects.filter(category="night")
            return render(request, 'night.html',{'rn':rn})
        else:
            ro = ritem.objects.filter(category="other")
            return render(request, 'other.html',{'ro':ro})

def rec(request):
    return render(request,'rec.html')
def cart_add_ritems(request,name):
    uname = request.session['user']
    user = User.objects.get(username=uname)
    item = get_object_or_404(items,name=name)
    #if store.objects.filter(items__name=name).count() == 0:
    if request.method == 'POST':
        qty = request.POST.get('qty')
        storeItem.quantity = qty
        cart_item = storeItem.objects.create(
                items=items,
                users=user,
                quantity=qty,
            )
    uname = request.session['user']
    user = User.objects.get(username=uname)
    cart_items = storeItem.objects.filter(users=user)
    amount = 0;
    for cart_item in cart_items:
        print(cart_item.quantity)
        print(cart_item.items.name)
        amount = amount + cart_item.quantity * cart_item.items.price
    print('amount is', amount)
    context = {
        'cart_items': cart_items,
        'total': amount,
    }
    return render(request,'cart.html', context)

from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Query_table  # Assuming you have a Query_table model for storing queries


def add_table(request):
    if request.method == "POST":
        # Extract form data

        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time = request.POST.get('time')
        category = request.POST.get('category')
        guest = request.POST.get('guest')

        # Save data to Query_table model
        query = Query_table(
            uname=name,
            dcategory=category,
            dicapacity=guest,  # Assuming you're using this field to store "guest" information
            diprice=f"{date} {time}",  # Combine date and time for saving (or create separate fields if needed)
        )
        query.save()

        # Redirect or show a success message
        return HttpResponse("Your query has been submitted successfully!")
    else:
        return render(request, 'table.html')  # Render your form template
from django.shortcuts import render
from .models import Item

def delights(request):
    items = Item.objects.all()  # Get all items (fertilizers)
    return render(request, 'delights.html', {'ritem': items})


from django.shortcuts import redirect, get_object_or_404
from .models import Item, Cart
from django.contrib.auth.models import User

def add_to_cart(request, name):
    if request.method == "POST":
        item = get_object_or_404(Item, name=name)  # Get the item by name
        qty = int(request.POST.get('qty', 0))  # Get the quantity from the form

        if qty > 0:
            user = request.user  # Get the current logged-in user
            cart_item, created = Cart.objects.get_or_create(user=user, item=item)  # Get or create a cart item
            cart_item.quantity += qty  # Update the quantity in the cart
            cart_item.save()

    return redirect('fertilizer_list')  # Redirect back to the fertilizer list page


def cart_view(request):
    if request.user.is_authenticated:
        cart_items = Cart.objects.filter(user=request.user)
        return render(request, 'cart.html', {'cart_items': cart_items})
    else:
        return redirect('login')  # Redirect to login page if user is not authenticated


from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required





@login_required
def cart_add(request, name):
    if request.method == 'POST':
        user = request.user  # Get the current logged-in user
        quantity = request.POST.get('qty')
        # Perform the action (e.g., add to cart)
        cart_item, created = CartItem.objects.get_or_create(user=user, name=name)
        cart_item.quantity += int(quantity)
        cart_item.save()
        return redirect('cart')  # Redirect to a cart summary page


# views.py
from django.shortcuts import render, redirect, get_object_or_404
from .models import Product, Cart, CartItem

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
    cart_item.save()
    return redirect('cart_detail')
# views.py example for displaying a product list in Django

# views.py example for displaying a product list in Django

def product_list(request):
    products = Product.objects.all()  # Fetch all products from the database
    return render(request, 'product_list.html', {'products': products})


def cart_detail(request):
    cart, created = Cart.objects.get_or_create(user=request.user)
    items = cart.items.all()
    total_price = sum(item.product.price * item.quantity for item in items)
    return render(request, 'cart_detail.html', {'cart': cart, 'items': items, 'total_price': total_price})

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    quantity = int(request.POST.get('quantity', 1))
    # Handle adding to cart logic
