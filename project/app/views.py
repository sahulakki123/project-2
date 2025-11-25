from django.shortcuts import render,redirect
from .models import Student,Query, itames
from django.urls import reverse
from urllib.parse import urlencode

# Create your views here.

def landing(req):
    return render(req, 'landing.html')

def Swiggy_Corporate(req):
    return render(req, 'Swiggy_Corporate.html')


def partner_with_us(req):
    return render(req, 'Partner_with_us.html')


def swiggy_neb(req):
    return render(req, 'swiggy_neb.html')

def Our_Businesses(req):
    return render(req, 'Our_Businesses.html')

def Delivering(req):
    return render(req, 'Delivering.html')



def signup(req):
    if req.method == 'POST':
        n = req.POST.get('name')
        e = req.POST.get('email')
        c = req.POST.get('contact')
        i = req.FILES.get('image')
        d = req.FILES.get('document')
        p = req.POST.get('pass')
        cp = req.POST.get('cpass')
        # print(n,e,c,i,d,p,cp)
        user = Student.objects.filter(email=e)
        if user:
            msg = "Email already exist"
            return render (req, 'signup.html', {'msg':msg})
        else:
            if p==cp:
                data = {
                    'name':n,'email':e,'contact':c,'image':i,'document':d,'password':p
                }
                Student.objects.create(name=n,email=e,contact=c,image=i,document=d,password=p)
                return render(req,'login.html')
            else:
                pmsg = "Password and Conform password not match"
                return render(req, 'signup.html',{'pmsg':pmsg})
    return render(req, 'signup.html')

def login(req):
    if req.method == "POST":
        e = req.POST.get("email")
        p = req.POST.get("Password")
        # print(e,p)
        # print(type(e),type(p))
        user = Student.objects.filter(email=e)
        if user:
            data = Student.objects.get(email=e)
            upass = data.password
            if upass == p:
                cart = {'user_id': None, 'cart':{'user_id':None,'cart':[]}}
                cart = req.session.get('cart',cart)
                cart['user_id']=data.id
                print(data.id)
                cart['cart']['user_id'] = data.id
                req.session['cart'] = cart
                return redirect('desshboard2')
            else:
                msg = "Email and password not match"
                return render(req, 'login.html',{'pmsg':msg,'email':e})
        else:
            return redirect('signup')
    return render(req,'login.html')


def desshboard2(req):
    # cart = {'user_id': None, 'cart':{'user_id':None,'cart':[]}}
    # cart = req.session.get('cart',cart)
    cart = req.session.get('cart',{})
    userid = cart['user_id']
    # print(userid)
    if userid:   
        l = len(cart['cart']['cart'])
        user = Student.objects.get(id=userid)
        data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
        all_carts = itames.objects.all()
        return render(req, 'desshboard2.html',{'data':data,'l':l,'items':all_carts})
    else:
        return redirect('login')

def addcart(req,pk):
    print(pk)
    cart = req.session.get('cart',{})
    cart['cart']['cart'].append(pk)
    req.session['cart'] = cart
    userid = cart['user_id']
    l = len(cart['cart']['cart'])
    user = itames.objects.get(id=userid)
    data = {'name':user.name, 'fess':user.fess}
    all_carts = itames.objects.all()
    return render(req, 'desshboard2.html',{'data':data,'l':l,'items':all_carts})
    
    
    
    
# def desshboard2(req):
#     return render(req, 'desshboard2.html')

def logout(req):
    data = req.session.get('id',None)
    req.session.flush()
    return redirect('landing')

def query(req):
    data = req.session.get('id',None)
    if data:
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
        return render(req, 'dashboard.html',{'data':data, 'query':'query'})
    else:
        return redirect('login')

def querydata(req):
    if req.method=="POST":  
        n = req.POST.get('name')
        e = req.POST.get('email')
        q = req.POST.get('query')
        print(n,e,q)
        Query.objects.create(name=n,email=e, query=q)
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
        return render(req, 'dashboard.html',{'data':data})
    
def showquery(req):
    pk = req.session['id']
    user = Student.objects.get(id=pk)
    data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
    e = user.email
    allquery = Query.objects.filter(email=e)
    return render(req, 'dashboard.html',{'data':data, 'allquery':allquery})

def delete(req, qpk):
    data = Query.objects.get(id = qpk)
    data.delete()
    pk = req.session['id']
    user = Student.objects.get(id=pk)
    data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
    e = user.email
    allquery = Query.objects.filter(email=e)
    return render(req, 'dashboard.html',{'data':data, 'allquery':allquery})

def edit(req,qpk):
    olddate = Query.objects.get(id = qpk)
    pk = req.session['id']
    user = Student.objects.get(id=pk)
    data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
    return render(req, 'dashboard.html',{'data':data, 'edit':olddate})


def update(req, qpk):
    if req.method=='POST':
        olddate = Query.objects.get(id = qpk)
        update_query=req.POST.get('query')
        olddate.query = update_query
        olddate.save()
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
        e = user.email
        allquery = Query.objects.filter(email=e)
        return render(req, 'dashboard.html',{'data':data, 'allquery':allquery})
    


def search(req):
    if req.method=="POST":
        search_value = req.POST.get('search')
        pk = req.session['id']
        user = Student.objects.get(id=pk)
        data = {'name':user.name,'email':user.email,'contact':user.contact,'image':user.image,'document':user.document,'password':user.password}
        e = user.email
        allquery=Query.objects.filter(query__icontains=search_value, email__icontains=e)
        return render(req, 'dashboard.html',{'data':data, 'allquery':allquery})