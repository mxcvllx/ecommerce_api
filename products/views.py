from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductListSerializer


@api_view(["GET"])
def get_products_list(request):
    products = Product.objects.order_by("-id")
    serializer = ProductListSerializer(products, many=True)
    return Response(serializer.data)
