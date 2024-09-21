from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from .models import Post, Board, Accounts
from Functions.Hash import Hashing
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone

# Create your views here.
def BoardPage(request, boardCategory, pageNumber): # 게시판
    boardTitle = ""
    data = list(Post.objects.values("title", "postid", "accountnickname_id", "createdtime").filter(boardname=boardCategory))
    match boardCategory:
        case "free":
            boardTitle = "자유"
        case "study":
            boardTitle = "공부"
        case _:
            return HttpResponseBadRequest("알수 없는 요청입니다.")

    variables = {'loggedin' : request.session["loggedin"], 'posts' : data, 'page' : pageNumber, 'boardtitle' : boardTitle, 'category' : boardCategory}
    return render(request, "board/BoardPage.html", variables)

def PostPage(request, boardCategory, pageNumber, postID): # 게시글 조회 함수
    try:
        data = Post.objects.all().filter(postid=postID).values()[0] # 게시글 DB 조회 (없을 시 out of index 발생)
        data["pageNum"] = pageNumber
        data["loggedin"] = request.session["loggedin"]
        # data의 구성요소 : 'postid', 'title', 'contents', 'createdtime', 'accountnickname_id'(작성자 id), 'boardname_id'(게시판 카테고리 정보), category, pageNum
        
        return render(request, "board/PostPage.html", data)
    except Exception as e:
        return HttpResponseBadRequest("찾을 수 없는 게시글입니다.")

def MakePostPage(request, boardCategory): # 게시글 작성 페이지
    variables = {'board' : boardCategory, "loggedin" : request.session["loggedin"]}
    return render(request, "board/makePost.html", variables)

@csrf_exempt

def SubmitPost(request, boardCategory): # 게시글 DB에 반영
    data = request.POST # 요청으로 오는 제목, 내용 가져오기
    category = Board.objects.get(boardname = boardCategory)
    author = Accounts.objects.get(nickname = request.session["nickname"]) # ****나중에 로그인 기능 구현하면 여기다가 게시자 id 넣을 것****
    
    postid = Hashing(request.session["nickname"] + str(timezone.now())) # 게시글 식별 코드 만드는 부분
    
    post = Post(postid=postid, title=data["title"], contents=data["contents"], createdtime=timezone.now(), accountnickname=author, boardname=category) # Post테이블에 데이터 Insert하는 부분
    post.save() # 저장
    return HttpResponse(f"<script>alert('게시글이 작성되었습니다'); window.location.href='/board/{boardCategory}/1'; </script>") # 응답