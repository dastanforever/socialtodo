var mongoose = require('mongoose');
var setting = require('../settings.js'); 

mongoose.connect(setting.dburl);

var TodoSchema = new mongoose.Schema({
    name: String,
    completed: Boolean,
    note: String,
    updated_at: { type: Date, default: Date.now }
});

// All database methods to be placed here (before compilation model).



var Todo = mongoose.model('Todo', TodoSchema);