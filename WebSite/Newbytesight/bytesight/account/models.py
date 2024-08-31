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