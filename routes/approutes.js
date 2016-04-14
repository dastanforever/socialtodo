var indexController = require('./index.js');
var todoController = require('./todo.js');
var userController = require('./user.js');


module.exports = {
    index: indexController.index,
    todo: todoController,
    user: userController.profile, 
};