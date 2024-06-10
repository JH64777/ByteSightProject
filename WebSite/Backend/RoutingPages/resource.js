const express = require("express");
const router = express.Router();
const path = require('path');

router.get("/", (req, res) =>{
    res.render("Resource.html", {
        loggedin : req.session.loggedin
    });
});

module.exports = router;