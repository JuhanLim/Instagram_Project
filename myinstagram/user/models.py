from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    '''
        유저 프로필 사진 
        유저 아이디 ( 닉네임. 화면에 표기할 이름 )
        유저 실제 이름 
        유저 이메일 주소 ( 회원가입 할때 사용하는 아이디)
        유저 비밀번호 
    '''
    profile_image= models.TextField()
    nickname = models.CharField(max_length=24,unique=True)
    name = models.CharField(max_length=24)
    email = models.EmailField(unique=True)
    
    USERNAME_FIELD = 'nickname'
    class Meta:
        db_table = "User"