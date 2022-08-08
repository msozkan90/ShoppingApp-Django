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