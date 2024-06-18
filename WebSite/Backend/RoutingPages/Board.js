const express = require("express");
const router = express.Router();
const Post = require("../DB/models/Post");

function CurrentTime(){ // 시간 반환 함수
    let now = new Date();
    let year = now.getFullYear(); // 년
    let month = (now.getMonth() + 1).toString().padStart(2, '0'); // 월
    let day = now.getDate().toString().padStart(2, '0'); // 일
    let hour = now.getHours().toString().padStart(2, '0'); // 시
    let minutes = now.getMinutes().toString().padStart(2, '0'); // 분
    let second = now.getSeconds().toString().padStart(2, '0'); // 초

    return `${year}${month}${day}${hour}${minutes}${second}`;
}

function Getposts(boardName, pageNum){ // 게시글들 가져오는 함수
    try {
        return Post.findAll({
            attributes : ['title', 'postID'],
            where : {
                boardname : boardName
            },
            offset : (pageNum - 1) * 5,
            limit : 5
        });
    } catch (error) {
        console.log(error);
    }
}

router.get("/:board/makepost", (req, res) => { // 게시글 생성
    if(req.session.loggedin)
        res.render("makePost.html", {
            loggedin : req.session.loggedin,
            board : req.params.board
        });
    else
        res.send(`<script>alert('해당 기능은 로그인이 필요합니다.'); 
        window.location.href = '${"/board/" + req.params.board + "/1"}';
        </script>`);
});

router.post("/:board/post/submit", (req, res) => { // 게시글 업로드와 관련된 부분 이제 해당 내용을 DB에 넣으면 됨
    if(req.session.loggedin){
        const time = CurrentTime();
        const usercode = req.body.title + req.session.userNick + time;

        Post.create({
            postID : usercode,
            title : req.body.title,
            contents : req.body.contents,
            createdtime : Date(time),
            accountNickname : req.session.userNick,
            boardname : req.params.board
        })

        res.send(`<script>alert('게시글 작성이 완료되었습니다.'); 
        window.location.href = '${"/board/" + req.params.board + "/1"}';
        </script>`);
    }
    else
        res.status(403).send("<h1>잘못된 접근입니다.(Error 403)</h1><hr>");
});

router.get("/:board/:num", async (req, res, next) =>{ // 게시판 페이지 별 조회
    
    const postlist = await Getposts(req.params.board, req.params.num);

    const sanitizedPosts = postlist.map(post => ({ // 필요한 정보만 추출
        title: post.dataValues.title,
        postID: post.dataValues.postID
    }));

    switch(req.params.board){
        case "study": // 공부 게시판
            res.render("StudyBoard.html", {
                loggedin : req.session.loggedin,
                posts : sanitizedPosts,
                page : req.params.num
            });
            break;
        case "free": // 자유 게시판
            res.render("FreeBoard.html", {
                loggedin : req.session.loggedin,
                posts : sanitizedPosts,
                page : req.params.num
            });
            break;
        default:
            next();
            break;
            
    }
});

router.get("/:board/:num/:postID", (req, res) => { // 게시글 조회
    res.send(req.params.postID + " Hello");
});

module.exports = router;