const express = require("express");
const router = express.Router();
const Post = require("../DB/models/Post");

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

router.get("/:board/makepost", (req, res) => {
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
        console.log(req.body.title);
        console.log(req.body.contents);
        res.send("Well!");    
    }
    else
        res.status(403).send("<h1>잘못된 접근입니다.(Error 403)</h1><hr>");
});

router.get("/:board/:num", async (req, res, next) =>{
    
    let postlist;

    switch(req.params.board){
        case "study": // 공부 게시판
            postlist = await Getposts(req.params.board, req.params.num);
            res.render("StudyBoard.html", {
                loggedin : req.session.loggedin,
                posts : postlist
            });
            break;
        case "free": // 자유 게시판
            postlist = await Getposts(req.params.board, req.params.num);
            res.render("FreeBoard.html", {
                loggedin : req.session.loggedin,
                posts : postlist
            });
            break;
        default:
            next();
            break;
            
    }
});

module.exports = router;