import os
from uuid import uuid4
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from user.models import User
from myinstagram.settings import MEDIA_ROOT
from .models import Feed , Reply , Like , Bookmark

# Create your views here.


class Sub(APIView):
    def get(self, request):
        
        email = request.session.get('email',None)
        
        if email is None:
            # 로그인 없이 접속했을 경우 
            return render(request,"user/login.html")
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            # 로그인 없이 접속했을 경우 
            return render(request,"user/login.html")
        
        feed_object_list = Feed.objects.all().order_by('-id') # = Select * from content_feed; 최근 순으로 가져오기 위해 -id 를 기준으로 가져온다
        # for feed in feed_list:
        #     print(feed)
        #print(Feed_list)
        feed_list =[]
        for feed in feed_object_list:
            feed_user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                reply_user = User.objects.filter(email=reply.email).first()
                reply_list.append(dict(
                    reply_content=reply.reply_content,
                    nickname=reply_user.nickname
                ))
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(feed_id=feed.id, email=email, is_like=True).exists()
            is_marked = Bookmark.objects.filter(feed_id=feed.id, email=email, is_marked=True).exists()
            feed_list.append(dict(
                id=feed.id,
                image=feed.image,
                content=feed.content,
                like_count=like_count,
                Profile_image=feed_user.profile_image,
                nickname=feed_user.nickname,
                reply_list=reply_list,
                is_liked=is_liked,
                is_marked=is_marked,
            ))

        return render(request, "myinstagram/main.html", context=dict(feeds=feed_list, user=user))    
        
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
        email = request.session.get('email',None)

        Feed.objects.create(image=image,content=content,email=email)
        
        return Response(status=200)
    
class Profile(APIView):
    def get(self, request):
        
        email = request.session.get('email',None)
        
        if email is None:
            # 로그인 없이 접속했을 경우 
            return render(request,"user/login.html")
        
        user = User.objects.filter(email=email).first()
        
        if user is None:
            # 로그인 없이 접속했을 경우 
            return render(request,"user/login.html")
        
        feed_list = Feed.objects.filter(email=email).all() # 내 이메일과 맞는 feed 리스트를 전부 담기 ( 내가쓴 피드 )
        like_list = list(Like.objects.filter(email=email, is_like = True).values_list('feed_id',flat=True)) # 내가 누른 좋아요 중에서 value_list 를 통해 feed_id 만 가져오고 , flat=True 를 통해 리스트로 받는다 -> 쿼리셋리스트라 다시한번 리스트 씌움
        
        # 좋아요를 누른 feed_id 를 가져오고 , 그 후에 그 id 에 맞는 실제 피드를 가져온다 
        
        like_feed_list = Feed.objects.filter(id__in=like_list)
        bookmark_list = list(Bookmark.objects.filter(email=email, is_marked=True).values_list('feed_id',flat=True))
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list)
        return render(request, 'content/profile.html',context = dict(feed_list=feed_list,
                                                                    user=user,
                                                                    like_feed_list = like_feed_list,
                                                                    bookmark_feed_list = bookmark_feed_list
                                                                    ))
    
class UploadReply(APIView):
    def post(self,request):
        feed_id = request.data.get('feed_id',None)
        reply_content = request.data.get('reply_content',None) # 나머지 데이터는 ajax 로 받을거임 
        email = request.session.get('email',None) # 이메일은 세션에서 
        Reply.objects.create(feed_id=feed_id, reply_content=reply_content,email=email)
        
        return Response(status=200)
    
class ToggleLike(APIView):
    def post(self,request):
        
         
        feed_id = request.data.get('feed_id',None)
        favorite_text = request.data.get('is_like',True) # 나머지 데이터는 ajax 로 받을거임 
        
        if favorite_text =="favorite_border": # 정보가 전달됬을때 border 면 좋아요x -> 좋아요를 누른거니까 
            is_like = True
        else : 
            is_like = False
        
        email = request.session.get('email',None) # 이메일은 세션에서
        like = Like.objects.filter(feed_id=feed_id,email=email).first() # 기존에 누른게 있는지 확인
        
        if like : 
            like.is_like = is_like
            like.save()
        else : 
            Like.objects.create(feed_id=feed_id, is_like=is_like,email=email)
        
        return Response(status=200)

class ToggleBookmark(APIView):
    def post(self,request):
        feed_id = request.data.get('feed_id',None)
        bookmark_text = request.data.get('bookmark_text',True) # 나머지 데이터는 ajax 로 받을거임 
        
        if bookmark_text =="bookmark_border": # 정보가 전달됬을때 border 면 좋아요x -> 좋아요를 누른거니까 
            is_marked = True
        else : 
            is_marked = False
        
        email = request.session.get('email',None) # 이메일은 세션에서
        bookmark = Bookmark.objects.filter(feed_id=feed_id,email=email).first() # 기존에 누른게 있는지 확인
        
        if bookmark : 
            bookmark.is_marked= is_marked
            bookmark.save() 
        else : 
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked,email=email)
        
        return Response(status=200)


    