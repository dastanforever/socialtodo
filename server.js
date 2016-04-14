var express = require('express');
var morgan = require('morgan');
var appsettings = require('./settings.js');
var routes = require('./routes/approutes.js');
var Model = require('./model/models.js')



// Url Configs.
var hostname = appsettings.hostname;
var port = appsettings.port;

// Express app.
var app = express();

// Development environment logging.
app.use(morgan('dev'));


// Attach the routers.

// Serve static files.
//app.use(express.static(__dirname + '/public'));

app.listen(port, hostname, function(){
    console.log('Server running at http://${hostname}:${port}/');
})

app.get("/", function(req, res){
    //res.send("Hello Guest!");
    var chris = Model.User({
        name: 'Pranav',
        age: 21,
        password: "abc",
    });
    
    chris.save(function(err){
        if (err)
            console.log("Failed save!!");
    });
    
    Model.User.find({}, function(err, users){
        if(err) throw err;
        res.send(users);
    });    
});
