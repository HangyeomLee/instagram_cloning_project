from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed

# Create your views here.
class Main_Content(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # 쿼리 셋임
        return render(request,"gyeomstagram\main.html", context = dict(feeds = feed_list))
    

class UploadFeed(APIView):
    def post(self, request):
        file = request.data.get('file')
        image = request.data.get('image')
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image = request.data.get('profile_image')

        print(file)
        print(image)

        return Response(status=200)