
from django.urls import path
from . import views
from django.conf import settings  
from django.conf.urls.static import static  
app_name="store"
urlpatterns = [


	
    path('', views.store, name="store"),
	path('edit/', views.list, name="edit"),
	path('page/man', views.man,name="man"),
	path('page/woman', views.woman,name="woman"),
	path('page/child', views.child,name="child"),
	path('page/home', views.home,name="home"),
	path('page/electronic', views.electronic,name="electronic"),
	path('page/coupon', views.coupon,name="coupon"),
	path('page/all', views.all,name="all"),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('register/', views.register, name="register"),
 	path('login/', views.sign_in, name="login"),
	path('logout/', views.sign_out, name="logout"),


	path('add_product/', views.addProduct, name="addProduct"),
    
	path('<str:name>/<str:category>', views.product,name="product"),
    path('<str:name>/<str:category>/<str:id>', views.detail,name="detail"),
	path('update_item/', views.updateItem, name="update_item"),
	
	path('cart/update_item/', views.updateItem, name="update_item"),
	path('<str:name>/<str:category>/update_item/', views.product, name="update_item"),
	path('process_order/', views.processOrder, name="process_order"),
	path('<str:name>/', views.categoryss, name="categoryss"),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)  