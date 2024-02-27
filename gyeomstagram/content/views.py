from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main_Content(APIView):
    def get(self, request):
        feed_list = Feed.objects.all() # 쿼리 셋임

        print(feed_list)


        return render(request,"gyeomstagram\main.html")
    