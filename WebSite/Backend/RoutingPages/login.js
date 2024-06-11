const express = require("express");
const router = express.Router();
const Account = require("../DB/models/Account");
const path = require('path');
const bcrypt = require("bcrypt");

router.get("/", (req, res) =>{
    if(req.session.loggedin) // 로그인 여부 확인
        res.status(403).send("<h1>이미 로그인이 되어 있습니다.</h1><hr>");
    else
        res.sendFile(path.join(__dirname, "../../Frontend/Views/login.html"));
});

router.post("/submit", async (req, res, next) =>{
    const info = await Account.findOne({
        where : {
            id : req.body.st_id,
        }
    });

    const checker = await bcrypt.compare(req.body.st_password, info.pwd);
    if(checker)
    {
        req.session.userNick = info.nickname; // 세션에 닉네임 저장
        req.session.loggedin = true; // 세션에 로그인 여부 저장
        res.send("<script>alert('로그인에 성공하셨습니다.'); window.location.href='http://localhost:8080';</script>");
    }
    else
        res.send("<script>alert('로그인에 실패하셨습니다.'); window.location.href='http://localhost:8080';</script>");
});

router.get("/logout", (req, res) =>{
    try{
        if(req.session.loggedin)
        {
            req.session.destroy(() => {
            res.clearCookie("session-cookie"); // 웹 브라우저에 남아 있는 세션 쿠키 제거
            res.send("<script>alert('로그아웃에 성공하셨습니다.'); window.location.href='http://localhost:8080';</script>");
            });
        }
        else
            res.status(403).send("<h1>잘못된 접근입니다.</h1><hr>");
    }catch{
        res.send("<script>alert('로그아웃에 실패하셨습니다.'); window.location.href='http://localhost:8080';</script>");
    }
    
});

module.exports = router;