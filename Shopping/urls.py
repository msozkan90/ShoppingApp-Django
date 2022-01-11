"""Shopping URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from store import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('store.urls')),

    path('api/', views.apiOverview, name="api-overview"),
	path('api/product-list/', views.productList, name="product-list"),
	path('api/product-detail/<str:id>/', views.productDetail, name="product-detail"),
	path('api/product-create/', views.productCreate, name="product-create"),
	path('api/product-update/<str:pk>/', views.productUpdate, name="product-update"),
	path('api/product-delete/<str:pk>/', views.productDelete, name="product-delete"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)