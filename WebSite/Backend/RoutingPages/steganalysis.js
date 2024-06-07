const express = require("express")
const router = express.Router();
const path = require('path');

router.get('/', (req, res) => {
    res.sendFile(path.join(__dirname, '../../Frontend/Views/analysis.html'));
});

router.get('/SubmitImage', (req, res) => {

});

module.exports = router;