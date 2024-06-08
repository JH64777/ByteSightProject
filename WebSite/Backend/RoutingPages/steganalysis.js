const express = require("express")
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../../Frontend/Views/analysis.html'));
});

router.get('/SubmitImage', (req, res) => {
    // 여기다가 인공지능 연결해서 하기
});

module.exports = router;