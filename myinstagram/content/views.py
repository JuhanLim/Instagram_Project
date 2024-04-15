import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from myinstagram.settings import MEDIA_ROOT
from .models import Feed

# Create your views here.


class Sub(APIView):
    def get(self, request):
        feed_list = Feed.objects.all().order_by('-id') # = Select * from content_feed; 최근 순으로 가져오기 위해 -id 를 기준으로 가져온다
        # for feed in feed_list:
        #     print(feed)
        #print(Feed_list)
        return render(request, "myinstagram/main.html", context = dict(feeds=feed_list))  # 3번째 인자값으로 context 를 넘길 수 있다. ( 키 이름은 설정 )
    
class UploadFeed(APIView):
    def post(self, request):
        
        file = request.FILES['file']
        
        uuid_name = uuid4().hex     #파일이름이 한글일 경우 오류날 수 있으므로 랜덤 저장
        save_path = os.path.join(MEDIA_ROOT, uuid_name) 
        
        with open(save_path, 'wb+') as destination:
            for chunk in file.chunks():
                destination.write(chunk)
        
        image = uuid_name
        content = request.data.get('content')
        user_id = request.data.get('user_id')
        profile_image=request.data.get('profile_image')

        Feed.objects.create(image=image,content=content,user_id=user_id,profile_image=profile_image,like_count=0)
        
        return Response(status=200)
    