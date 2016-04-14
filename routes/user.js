var express = require('express');
var profile = express.Router();

profile.get('/', function(req, res){
    res.send("User Home"); 
});

profile.get('/settings', function(req, res) {
    res.send("User settings page.");
});




module.exports = profile;