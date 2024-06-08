const express = require("express");
const router = express.Router();
const path = require('path');

router.get("/", (req, res) =>{
    res.sendFile(path.join(__dirname, "../../Frontend/Views/account.html"));
});

router.post("/check", (req, res) => {
    let id = req.body.id;
    
    res.send(JSON.stringify({msg : "Your Message is sent well!"}));
});

module.exports = router;