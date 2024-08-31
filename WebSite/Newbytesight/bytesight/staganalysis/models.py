from django.db import models

# Create your models here.
class Accounts(models.Model): # 회원 관련 정보 table
    nickname = models.CharField(primary_key=True, max_length=20)
    id = models.CharField(unique=True, max_length=20)
    pwd = models.CharField(max_length=64)
    email = models.CharField(max_length=30)

    class Meta:
        managed = False
        db_table = 'accounts'

class SteganalysisIMG(models.Model):
    uploaded_date = models.DateTimeField(auto_now_add=True)
    imgfile = models.ImageField(null=True, upload_to="", blank=True) # 한 디렉토리 안에 파일 양이 많아지면 성능저하를 일으킨다고 한다. (media/년/월/일/사진파일.jpg 등으로 설정)