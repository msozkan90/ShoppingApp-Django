from rest_framework import serializers
# from SHOPPING.store.models import Product

from .models import Product

class ProductSerializer(serializers.ModelSerializer):
	class Meta:
		model = Product
		fields ='__all__'