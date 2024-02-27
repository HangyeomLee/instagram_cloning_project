from django.db import models

# Create your models here.
class Feed(models.Model):
    id = models.AutoField(primary_key=True)
    content = models.TextField() # 글내용 
    image = models.TextField() # 피드 이미지
    profile_image = models.TextField() # 프로필 사진
    user_id = models.TextField() # 글쓴이 아이디
    like_count = models.IntegerField() # 좋아요 수(사실 안씀)