const express = require("express");
const router = express.Router();
const path = require('path');

router.get("/", (req, res) =>{
    res.sendFile(path.join(__dirname, "../../Frontend/Views/login.html"));
});

router.post("/", (req, res) =>{
    res.send("Hello");
});

module.exports = router;