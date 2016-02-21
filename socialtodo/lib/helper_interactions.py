



from socialtodo.model.todo import todoItems as T
from socialtodo.model.auth import User as U


class Interactions:
    """docstring for Interactions

    All the interactions between user and her todo.
    """

    def getnotifdoc(self, by_id, for_id, madebyusername):
        notif = {
            'madebyid': by_id,
            'madeforid': for_id,
            'madebyusername': madebyusername,
        }
        return notif

    def getuser(self, username):
        return U.User.query.find({'username': username}).first()

    def getAllUserToDo(self, user_id):
        todoList = T.query.find(user_id = user_id).all()

    def managerelation(self, typeofrelation, meusername, tousername):
        res = ""
        if typeofrelation == "sendrequest":
            res = self.sendrequestutu(meusername, tousername)
        elif typeofrelation == "cancelrequest":
            self.cancelrequestutu(meusername, tousername)
        elif typeofrelation == "acceptrequest":
            res = self.acceptrequestutu(meusername, tousername)
        elif typeofrelation == "removefriend":
            self.removefriend(meusername, tousername)
        if res != "":
            return res
        else:
            return None

    def sendrequestutu(self, meusername, tousername):
#       If user is confirmed then only.
        meuser = self.getuser(meusername)
        touser = self.getuser(tousername)
        meuser['sentrequests'].append(touser['_id'])
        touser['recievedrequests'].append(meuser['_id'])
        notifdoc = self.getnotifdoc(meuser._id, touser._id, meuser.username)
        notif = N.Notifications()
        notif = notif.readynotif('friendrequest', notifdoc)
        touser.notifications.append(notif['_id'])
        s.session.flush()
        return [touser._id, notif]

    def acceptrequestutu(self, meusername, fromusername):
#       If users are confirmed, only then.
        meuser = self.getuser(meusername)
        fromuser = self.getuser(fromusername)
        meuser['recievedrequests'].remove(fromuser['_id'])
        fromuser['sentrequests'].remove(meuser['_id'])
        meuser['friends'].append(fromuser['_id'])
        fromuser['friends'].append(meuser['_id'])
        notifdoc = self.getnotifdoc(meuser._id, fromuser._id, meuser.username)
        notif = N.Notifications()
        notifdoc['status'] = 'accepted'
        notif = notif.readynotif('friendrequestack', notifdoc)
        fromuser.notifications.append(notif['_id'])
        s.session.flush()
        return [fromuser._id, notif]

    def cancelrequestutu(self, meusername, tousername):
        meuser = self.getuser(meusername)
        touser = self.getuser(tousername)
        meuser['sentrequests'].remove(touser['_id'])
        touser['recievedrequests'].remove(meuser['_id'])
        s.session.flush()

    def rejectrequestutu(self, meusername, fromusername):
        meuser = self.getuser(meusername)
        fromuser = self.getuser(fromusername)
        meuser['recievedrequests'].remove(fromuser['_id'])
        fromuser['sentrequests'].remove(meuser['_id'])
        notifdoc = self.getnotifdoc(meuser._id, fromuser._id, meuser.username)
        notif = N.Notifications()
        notifdoc['status'] = 'rejected'
        notif = notif.readynotif('friendrequestack', notifdoc)
        fromuser.notifications.append(notif['_id'])
        s.session.flush()
        return [fromuser._id, notif]

    def removefriend(self, meusername, tousername):
        meuser = self.getuser(meusername)
        touser = self.getuser(tousername)
        meuser['friends'].remove(touser['_id'])
        touser['friends'].remove(meuser['_id'])
        s.session.flush()

    def checkfriends(self, meuser, touser):
        if touser._id in meuser['friends']:
            return True
        return False

    def relstatus(self,fromuser, touser):
#       Check all the four possibilities
#       possibility 1, is user friends.
        for friend in fromuser['friends']:
            if touser['_id'] == friend:
                return 0

#       If fromuser has sent request to touser
        for friend in fromuser['sentrequests']:
            if touser['_id'] == friend:
                return 1

#       if touser has sent request to fromuser
        for friend in touser['sentrequests']:
            if fromuser['_id'] == friend:
                return 2

#       if both are not related at all
        return 3
