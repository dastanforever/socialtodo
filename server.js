var express = require('express');
    
var morgan = require('morgan');

var hostname = 'localhost';
var port = 3000;

var app = express();

// Development environment logging.
app.use(morgan('dev'));

// Serve static files.
app.use(express.static(__dirname + '/public'));

app.listen(port, hostname, function(){
    console.log('Server running at http://${hostname}:${port}/');
})