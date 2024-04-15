from django.db import models

# Create your models here.

class Feed(models.Model): # models.Model 상속
    content       = models.TextField()      #글내용
    image         = models.TextField()      # 피드 이미지    #이미지 url 을 사용할것이므로
    # profile_image = models.TextField()      # 프로필 이미지
    # user_id       = models.TextField()      # 글쓴이  -> 피드에서 받을 필요가 없음. 
    email         = models.EmailField(default='')
    #like_count    = models.IntegerField()   # 좋아요 수 , Like 모델에서 직접 가져올거라서 삭제
    
class Like(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_like = models.BooleanField(default=True)
    
class Reply(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    reply_content = models.TextField()
    

class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)
    email = models.EmailField(default='')
    is_marked = models.BooleanField(default=True)
    
