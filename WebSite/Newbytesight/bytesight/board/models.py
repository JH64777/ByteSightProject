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

class Board(models.Model): # 게시판 관련 정보 table
    boardname = models.CharField(primary_key=True, max_length=40)

    class Meta:
        managed = False
        db_table = 'board'

class Post(models.Model): # 게시글 관련 정보 table
    postid = models.CharField(db_column='postID', primary_key=True, max_length=64)  # Field name made lowercase.
    title = models.CharField(max_length=40)
    contents = models.TextField()
    createdtime = models.DateTimeField()
    accountnickname = models.ForeignKey(Accounts, models.DO_NOTHING, db_column='accountNickname', blank=True, null=True)  # Field name made lowercase.
    boardname = models.ForeignKey(Board, models.DO_NOTHING, db_column='boardname', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'post'