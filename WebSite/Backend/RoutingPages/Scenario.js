const express = require("express")
const router = express.Router();
const path = require('path');

router.get('/:num', (req, res, next) => {
        try {
            if(req.params.num == 1)
                res.download(path.join(__dirname, '../../Frontend/Download/Scenario1.zip'));
            else if(req.params.num == 2)
                res.download(path.join(__dirname, '../../Frontend/Download/test.zip'));
            else
                next();
        } catch (error) {
            console.log(error);
        }
    });

module.exports = router;