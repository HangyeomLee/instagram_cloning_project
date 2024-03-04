from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser

# Create your models here.
class User(AbstractBaseUser):
    # 유저 프로필 사진이랑 아이디(닉네임), 유저 이멜주소 비밀번호도 있어햐함 
    # 유저 이름도 있어야 함 실제 사용자 이름으로다가

    profile_image = models.TextField()
    nickname = models.CharField(max_length=24,unique = True)
    name = models.CharField(max_length=24)
    email = models.CharField(max_length = 50)

    USERNAME_FIELD = 'nickname'


    class Meta:
        db_table = "User"