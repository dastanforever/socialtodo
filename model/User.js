var mongoose = require('mongoose');
var setting = require('../settings.js'); 

mongoose.connect(setting.dburl);

var UserSchema = new mongoose.Schema({
    name: String,
    age: number,
});


// All database methods to be placed here (before compilation model).

var User = mongoose.model('User', UserSchema);