import imp
from django.shortcuts import redirect, render
from .forms import ProductForm, UserForm
from .models import user,products


def index(request):
    return redirect("/home")

def home(request):
    return render(request,"index.html")
   
def users(request):
    UsersData = user.objects.all()
    return render(request,'users.html',{'users':UsersData})


def product(request):
    ProductsData = products.objects.all()
    return render(request,'products.html',{'product':ProductsData})


def recommendations(request):
    return render(request,'hi')


def addproduct(request):
    if request.method == "POST":
        print("form submit-----------------")
        form = ProductForm(request.POST)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
            print("form valid-----------------")
        try:
            form.save()
            print("product successsfully Added------")
            return redirect("/products")
        except:
            return render(request,"addproduct.html")
    else:
        return render(request,"addproduct.html")



def adduser(request):
    if request.method == "POST":
        print("form submit-----------")
        form = UserForm(request.POST)
        print(form)
        print(form.cleaned_data)
        if form.is_valid():
                print('form valid--------------')
        try:
            form.save()
            print("User successfully added")
            return redirect('/users')
        except:
            return render(request,'adduser.html')
    else:
        return render(request,'adduser.html')
    


def edituser(request,id):
    if request.method == "POST":
        UserData = user.objects.get(id= id)
        print("edition submitted-----------")
        form = UserForm(request.POST, instance = UserData) 
        if form.is_valid():
            form.save()  
            return redirect("/users") 
        else:
            print(form.errors) 
            return render(request,'edituser.html',{'user': UserData})
    else:
        UserData = user.objects.get(id= id)
        return render(request,'edituser.html',{'user':UserData})

# def edituser(request,id):
#     UserData = user.objects.get(id = id)
#     return render(request,'edituser.html', {'user':UserData})


def editproduct(request,id):
    if request.method == "POST":
        ProductData = products.objects.get(id= id)
        print("edition submitted-----------")
        form = ProductForm(request.POST, instance = ProductData) 
        if form.is_valid():
            form.save()  
            return redirect("/products") 
        else:
            print(form.errors) 
            return render(request,'editproduct.html',{'product': ProductData})
    else:
        ProductData = products.objects.get(id= id)
        return render(request,'editproduct.html',{'product':ProductData})



def viewuser(request,id):
    UserData = user.objects.get(id = id)
    return render(request,"viewuser.html",{'user':UserData})


def viewproduct(request,id):
    ProductData = products.objects.get(id=id)
    return render(request,"viewproduct.html",{'product':ProductData})

