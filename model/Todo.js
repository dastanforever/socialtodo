var mongoose = require('mongoose');


mongoose.connect('mongodb://localhost/testtodo');

var TodoSchema = new mongoose.Schema({
    name: String,
    completed: Boolean,
    note: String,
    updated_at: { type: Date, default: Date.now }
});

var Todo = mongoose.model('Todo', TodoSchema);