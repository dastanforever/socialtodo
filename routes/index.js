


// Index Home for a user. 

app.get("/", function(req, res){
    res.send("Hello Guest!");
});

app.post("/", function(req, res){
    res.send("POST NOT ALLOWED");
});

app.route('/login')
    .get(function(req, res) {
        res.send("Login Page");
    });