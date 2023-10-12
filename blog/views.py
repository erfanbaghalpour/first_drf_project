from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
import requests
from .serializers import UserSerializer, ArticleSerializer
from django.contrib.auth.models import User
from .models import Article

URL = 'https://api.binance.com/api/v3/ticker/price?symbol=BTCUSDT'


@api_view(["GET", "POST"])
def hello_world(request):
    products = [
        {"name": "iphone 13",
         "price": "38 000 000"},
        {"name": "laptop",
         "price": 50000000}
    ]
    return Response(products)


class HelloWorld(APIView):
    def get(self, request):
        products = [
            {"name": "iphone 13",
             "price": "38 000 000"},
            {"name": "laptop",
             "price": 50000000}
        ]
        return Response(products)

    def post(self, request):
        return Response({"message": "I am from class based view"})


# search like this : http://127.0.0.1:8000/crypto?coin=btcusdt and The price will be displayed to you.
# instead of btcusdt you can sedarch others coins.

class GetCryptoPrice(APIView):
    def get(self, request):
        # coin = request.GET.get('coin')
        # response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin.upper()}")
        # data = response.json()
        # result = {
        #     "symbol": data['symbol'],
        #     "price": data['price'],
        # }
        queryset = User.objects.all()
        ser = UserSerializer(instance=queryset, many=True)

        return Response(data=ser.data)


# Article Serializer
class ArticleListView(APIView):
    def get(self, request):
        queryset = Article.objects.all()
        serializer = ArticleSerializer(instance=queryset, many=True)
        return Response(serializer.data)


class ArticleDetailView(APIView):
    def get(self, request, pk):
        instance = Article.objects.get(id=pk)
        serializer = ArticleSerializer(instance=instance)
        return Response(serializer.data)


class AddArticleView(APIView):
    def post(self, request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"response": "added"})
        return Response(serializer.errors)