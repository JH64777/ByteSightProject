const express = require("express")
const router = express.Router();
const upload = require("../Operations/ImgProcess");


router.get('/', (req, res) => {
    res.render("analysis.html", {
        loggedin : req.session.loggedin
    });
});

router.post('/SubmitImage', upload.single('AI_Img'), (req, res) => {
    console.log(req.file);
    res.send("IMG Submit");
});

module.exports = router;