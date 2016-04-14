var express = require('express');
var index = express.Router();
var Model = require('../model/models.js')


// Index Home for a user. 
index.get("/", function(req, res){
    res.send("Hello Guest!");
});

index.post("/", function(req, res){
    res.send("POST NOT ALLOWED");
});

index.route('/login')
    .get(function(req, res) {
        res.send("Login Page");
});





module.exports = index;