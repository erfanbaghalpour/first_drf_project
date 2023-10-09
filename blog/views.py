from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


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
