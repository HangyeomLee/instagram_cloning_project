from django.shortcuts import render
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main_Content(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # 쿼리 셋임
        return render(request,"gyeomstagram\main.html", context = dict(feeds = feed_list))