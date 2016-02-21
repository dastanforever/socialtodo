



from socialtodo.model.auth import User as U
from socialtodo.model.todo import toDoItem as T


class UserHelper:
    
    def getUser(self, username):
        return U.User.query.find({'username':username}).first()

    def getstatus(self, user):
        return user['status']

    def getAllUsers(self):
        return U.User.query.find().all()

    def getAllTodo(self):
        return T.toDoItem.query.find().all()

    def getRecentTodo(self, user):
        user = U.User.query.get(username=username)
        todoitems = []
        for todoid in user._todoitems:
            todoitems.append(T.toDoItem.query.get(_id=todoid))
            if len(todoitems) == user.homeRecentQuery:
                break
        todoitems.sort(key=lambda x: x.todoStartDateTime)
        return todoitems

    def modifyUser(self, username, doc):
        user = U.User.query.get(username=username)
        user.modify(doc)
        s.session.flush()
        return user

    def createToDo(self, doc):
        # Check if user is confirmed.
        user = U.User.query.find({'username':doc['username']})
#        if user.isConfirmed() == False:
#           return None
#        if not user.createToDoEligible():
#           return None
        td = T.toDoItem()
#        Verifications
        td.register_todo(doc)
        user.addToDo(td)
#        td.m.save()
        s.session.flush()
        return td

#    def getSearchResults(self, query):
#        text_results = s.pymongodb.command('text', 'users', search=query, limit=10)
#        return text_results['results']

    def getnotif(self, _id):
        return N.query.find({'_id':_id})

        