const express = require("express");
const router = express.Router();
const path = require('path');
const Account = require("../DB/models/Account");
const bcrypt = require("bcrypt");

async function Hashing(plain){
    const salt = await bcrypt.genSalt(10);
    const hashingString = await bcrypt.hash(plain, salt);
    return hashingString;
}

router.get("/", (req, res) =>{
    res.render("account.html", {
        loggedin : req.session.loggedin
    });
});

router.post("/check", async (req, res) => {
    let checkContents = req.body.contents;
    if(req.body.flag == "ID"){
        const result = await Account.findAll({
            where : {
                id : checkContents
            }
        });
        if(result.length == 0)
            res.send(JSON.stringify({msg : "사용 가능한 아이디 입니다", flag : true}));
        else
            res.send(JSON.stringify({msg : "이미 존재하는 아이디 입니다", flag : false}));
    }
    else{
        const result = await Account.findAll({
            where : {
                nickname : checkContents
            }
        });
        if(result.length == 0)
            res.send(JSON.stringify({msg : "사용 가능한 닉네임 입니다", flag : true}));
        else
            res.send(JSON.stringify({msg : "이미 존재하는 닉네임 입니다", flag : false}));
    }
});

router.post("/submit", async (req, res) => {
    try {
        Account.create({ 
            nickname : req.body.st_nickname,
            id : req.body.st_id,
            pwd : await Hashing(req.body.st_password),
            email : req.body.st_mail
        });
        res.redirect("/");
    } catch (error) {
        res.status(503).send("예기치 못한 에러가 발생하였습니다.");
    }
});

module.exports = router;