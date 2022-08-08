from django.shortcuts import render,redirect,get_object_or_404
from django.http import JsonResponse
import json
import datetime
from store.models import *
from django.contrib import messages
from .utils import cookieCart,cartData,guestOrder
from django.contrib.auth.forms import AuthenticationForm
from .forms import CreateUserForm
from .forms import ProductForm
from django.contrib.auth import login,logout,authenticate
from django.db import models

# Create your views here.
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from store.serializers import ProductSerializer
from .models import Product

# Create your views here.
@api_view(['GET'])
def apiOverview(request):
	api_urls = {
		'List':'/api-list/',
		'Detail View':'/api-detail/<str:pk>/',
		'Create':'/api-create/',
		'Update':'/api-update/<str:pk>/',
		'Delete':'/api-delete/<str:pk>/',
		}

	return Response(api_urls)

@api_view(['GET'])
def productList(request):
	tasks = Product.objects.all().order_by('-id')
	serializer = ProductSerializer(tasks, many=True)
	return Response(serializer.data)

@api_view(['GET'])
def productDetail(request, pk):
	tasks = Product.objects.get(pk=id)
	serializer = ProductSerializer(tasks, many=False)
	return Response(serializer.data)


@api_view(['POST'])
def productCreate(request):
	serializer = ProductSerializer(data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)

@api_view(['POST'])
def productUpdate(request, pk):
	task = Product.objects.get(id=pk)
	serializer = ProductSerializer(instance=task, data=request.data)

	if serializer.is_valid():
		serializer.save()

	return Response(serializer.data)


@api_view(['DELETE'])
def productDelete(request, pk):
	task = Product.objects.get(id=pk)
	task.delete()

	return Response('Item succsesfully delete!')

def list(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	form = ProductForm()
	context={"items":items ,"order":order,"cartItems":cartItems,"form":form}
	return render(request, 'store/edit.html',context)

def store(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']	
	products=Product.objects.all()
	categorys=Category.objects.all()
	main_category=MainCategory.objects.all()
	context={"items":items ,"order":order,"products":products,"cartItems":cartItems,"categorys":categorys,"main_category":main_category}
	return render(request,"store/store.html",context)

def register(request):
	
	data = cartData(request)
	cartItems=data['cartItems']
	form=CreateUserForm()
	if request.method == 'POST':
		form = CreateUserForm(request.POST)
		if form.is_valid:
			user = form.save(commit=False)
			user.save()
			messages.success(request,"You are registered successfully")
			return redirect("store:login")   
	return render(request,"store/register.html",{"form":form,"cartItems":cartItems})
def addProduct(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']	
	form = ProductForm()
	if request.method == 'POST':
		form = ProductForm(request.POST, request.FILES)
		print(form.errors)
		if form.is_valid:
	
			product = form.save(commit=False)
			product.save()
			messages.success(request,"You are add product successfully")
			context={"form":form,"product":product}
			return redirect("store:store")

	context={"items":items ,"order":order,"cartItems":cartItems,"form":form}
	return render(request,"store/add_product.html",context)
def updateItem(request):
	data = json.loads(request.body)
	productId = data['productId']
	action = data['action']
	print('Action:', action)
	print('Product:', productId)
	customer = request.user.customer
	product = Product.objects.get(id=productId)
	order, created = Order.objects.get_or_create(customer=customer, complete=False)
	orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

	if action == 'add':
		orderItem.quantity = (orderItem.quantity + 1)
	elif action == 'remove':
		orderItem.quantity = (orderItem.quantity - 1)

	orderItem.save()

	if orderItem.quantity <= 0:
		orderItem.delete()

	return JsonResponse('Item was added', safe=False)





def sign_in(request):
	form=AuthenticationForm()
	if request.method == 'POST':
		username = request.POST.get('username')
		password =request.POST.get('password')

		user = authenticate(request, username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, 'You are logged in succesfully')
			return redirect('store:store')
		else:
			messages.info(request, 'Username OR password is incorrect')

		context = {"form":form}
	
		return render(request, 'store/login.html', context)
	context = {"form":form}
	return render(request, 'store/login.html', context)
def sign_out(request):
	logout(request)
	messages.success(request, "You are logged out succesfully")
	return redirect("store:store")

def cart(request):
    data = cartData(request)
    cartItems=data['cartItems']
    items= data['items']
    order= data['order']

            
    context={"items":items ,"order":order,"cartItems":cartItems}
    return render(request,"store/cart.html",context)

def checkout(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	context={"items":items ,"order":order,"cartItems":cartItems,'shipping':False}


	return render(request, 'store/checkout.html', context)

def categoryss(request,name):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	category=MainCategory.objects.filter(name=name)
	categoryy=list(category)
	m=0
	
	for i in categoryy:
		if m==0:
			cate_name=i
			cate=cate_name
			m+=1
			products=Category.objects.filter(category=cate)
			context={"items":items ,"order":order,"cartItems":cartItems,"products":products,"category":category,"cate":cate}
			return render(request,"store/category_detail.html",context)
	context={"items":items ,"order":order,"cartItems":cartItems,"category":category}
	return render(request,"store/category_detail.html",context)


def product(request,name,category):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	categoryy=MainCategory.objects.filter(name=name)
	categoryy=list(categoryy)
	for i in categoryy:
		print(i)
		cate=i
	product=Product.objects.all()
	a=0
	b=-1
	liste2=[]
	liste=[]
	at1=[]
	at2=()
	at3=[]
	for i in product:
		at1=list(at1)		
		liste.append(i.name)		
		if  str(i.category) == str(category) :			
			c=b
			b+=1
			c=b			
			liste2.append(liste[c])
			x=liste[c]
			y=i.imageURL
			z=i.id
			at1.append(x)			
			at1.append(y)
			at1.append(z)
			at1=tuple(at1)
			at2=(at1,)
			at3+=at2
			at1=()
		else:			
			b+=1
			a+=1
	if len(liste2) == 0:
		data = cartData(request)
		items= data['items']
		order= data['order']
		cartItems=data['cartItems']
		#category=get_object_or_404(MainCategory,name=name)
		category=MainCategory.objects.filter(name=name)
		#cate_name=category
		cate=category[0]
		products=Category.objects.filter(category=cate)
		context={"items":items ,"order":order,"products":products,"cartItems":cartItems,"category":category,"cate":cate}
		messages.warning(request,"There is no any item in this category")
		return render(request,"store/category_detail.html",context)		
	context={"items":items ,"order":order,"product":product,"cartItems":cartItems,"categoryy":categoryy,"at3":at3,"liste2":liste2,"category":category,"cate":cate}
	return render(request,"store/product_detail.html",context)

def detail(request,name,category,id):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']

	#category=get_object_or_404(MainCategory,name=name)
	categoryy=MainCategory.objects.filter(name=name)
	cate_name=categoryy
	cate=cate_name[0]
	products=Product.objects.all()
	
	for i in products:
		if str(i.id) == str(id):
			print(i.id)
			print(i.price)
			print(i.image)
			detail=i
	#products=get_object_or_404(Category,category=)
	context={"detail":detail,"items":items ,"order":order,"products":products,"cartItems":cartItems,"category":category,"id":id,"cate":cate}
	return render(request,"store/detail.html",context)







def processOrder(request):
	transaction_id = datetime.datetime.now().timestamp()
	data = json.loads(request.body)

	if request.user.is_authenticated:
		customer = request.user.customer
		order, created = Order.objects.get_or_create(customer=customer, complete=False)
	else:
		customer, order = guestOrder(request, data)

	total = float(data['form']['total'])
	order.transaction_id = transaction_id

	if total == order.get_cart_total:
		order.complete = True
	order.save()

	if order.shipping == True:
		ShippingAddress.objects.create(
		customer=customer,
		order=order,
		address=data['shipping']['address'],
		city=data['shipping']['city'],
		state=data['shipping']['state'],
		zipcode=data['shipping']['zipcode'],
		)

	return JsonResponse('Payment submitted..', safe=False)

def showpage1(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	#category=get_object_or_404(MainCategory,name=name)
	product=Product.objects.all()
	products=[]
	for i in product:
		
		if str(i.category.category) == "Man":
			print(i)
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )



def man(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		
		if str(i.category.category) == "Man":
			
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def woman(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		
		if str(i.category.category) == "Woman":
			
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def child(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		
		if str(i.category.category) == "Child":
			
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def home(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		
		if str(i.category.category) == "Home":
			
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def electronic(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		print(i.category.category)
		if str(i.category.category) == "Electronic":
			
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def coupon(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	product=Product.objects.all()
	products=[]
	for i in product:
		print(i.category.category)
		if str(i.category.category) == "Product Coupons":
		
			products.append(i)
	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

def all(request):
	data = cartData(request)
	cartItems=data['cartItems']
	items= data['items']
	order= data['order']
	products=Product.objects.all()

	
	context={"items":items ,"order":order,"cartItems":cartItems,"products":products}
	return render(request,"store/man.html", context )

