var express = require('express');
var router = express.Router();

router.get('/', function(req, res){
    res.send("User Home"); 
});

router.get('/settings', function(req, res) {
    res.send("User settings page.");
});




module.exports = router;