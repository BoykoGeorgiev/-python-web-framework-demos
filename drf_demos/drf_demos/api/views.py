from rest_framework import generics as api_views
# from rest_framework import views as api_views
from rest_framework import serializers

from rest_framework.response import Response

from drf_demos.api.models import Product, Category


class IdAndNameCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class FullCategorySerializer(serializers.ModelSerializer):


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'
        # fields = ('id', 'name')


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()

    class Meta:
        model = Product
        fields = '__all__'


# class ProductsListView(api_views.APIView):
#     def get(self, request):
#         products = Product.objects.all()
#         serializer = ProductSerializer(products, many=True)
#
#         return Response(data=serializer.data)
#
#     def post(self, request):
#         serializer = ProductSerializer(data=request.data, many=False)
#         if serializer.is_valid():
#             print(serializer.validated_data)
#             return Response(status=201)
#         return Response(serializer.errors, status=400)


class ProductsListView(api_views.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        return super().perform_create(serializer)


class CategoriesListView(api_views.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class SingleProductView(api_views.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

