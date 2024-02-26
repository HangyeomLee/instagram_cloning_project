from django.shortcuts import render
from rest_framework.views import APIView

class Main(APIView):
    def get(self, request):
        print("겟으로 받음")
        return render(request,"gyeomstagram\main.html")
    
    def post(self, request):
        print("포스트로 받음")
        return render(request,"gyeomstagram/main.html")