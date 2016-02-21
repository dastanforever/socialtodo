# -*- coding: utf-8 -*-
"""
Auth* related model.

This is where the models used by the authentication stack are defined.

It's perfectly fine to re-use this definition in the socialtodo2 application,
though.

"""

from ming import schema
from ming.odm import MappedClass
from ming.odm import FieldProperty
from session import DBSession
import bcrypt
import datetime


class EmailAddress(MappedClass):
    """docstring for EmailAddress"""

    class __mongometa__:
        session = DBSession
        name = "emailaddress"

    _id = FieldProperty(schema.ObjectId)
    emailid = FieldProperty(schema.String)
    claimedbyuserid = FieldProperty(schema.ObjectId)
    hashcode = FieldProperty(schema.String)


class User(MappedClass):
    """docstring for User
    Indexing fields -
    1. Userid,username
    2. username, userid     # Check if different
    """

    class __mongometa__:
        session = DBSession
        name = "users"
        unique_indexes = [('username', 'emailid',)]
        indexes = [ ('username'),
                    ('status'),
                ]
        custom_indexes = [
                dict(
                    fields=[
                            ('username', 'text'),
                            ('firstname', 'text'),
                            ('lastname', 'text'),
                            ('organization', 'text'),
                            ], name="search_index", weights={
                                                                'firstname': 100,
                                                                'organization': 100,
                                                                'lastname': 80,
                                                                'username':60,
                            })
        ]

    _id = FieldProperty(schema.ObjectId)
    username = FieldProperty(schema.String)
    firstname = FieldProperty(schema.String)
    lastname = FieldProperty(schema.String)
    password = FieldProperty(schema.String)
    emailid = FieldProperty(schema.String)
    confirmed = FieldProperty(schema.Bool)
    account_created = FieldProperty(schema.DateTime)
    status = FieldProperty(schema.String)
    organization = FieldProperty(schema.String)
    numberoflogins = FieldProperty(schema.Int)
    dailyscheduleid = FieldProperty(schema.ObjectId)

#   To do creation props.
    limit_todo = FieldProperty(schema.Int)
    created_todo = FieldProperty(schema.Int)
    nextToDoDateTime = FieldProperty(schema.DateTime)

#   To Do props
#   Created by others, but sent to you. Key value pair of toobjectid and userobjectid(requester).
#   If accepted reqests, _todoitems will have the items. Else nothing. But removing from this list is common.
    todorecievedrequests = FieldProperty(schema.Array(schema.Object))
#   Created by you/ currently assigned to you and sent to others. Just todoid stored.
#   If accepted, then list will remove the item. Else, it will be added to _todoitems with
#   assigned to you.
    todosentrequests = FieldProperty(schema.Array(schema.ObjectId))

#   Notifications
    notifications = FieldProperty(schema.Array(schema.ObjectId))

#   A dict link object. { Key = ObjectID : Value = assignedID}
#   Only for self created todo's.
    _todoitems = FieldProperty(schema.Array(schema.ObjectId))

#   Friends prop.
    friends = FieldProperty(schema.Array(schema.ObjectId))
    sentrequests = FieldProperty(schema.Array(schema.ObjectId))
    recievedrequests = FieldProperty(schema.Array(schema.ObjectId))
    totalfriends = FieldProperty(schema.Int)

#   Teams prop.
    teams = FieldProperty(schema.Array(schema.ObjectId))
    sentrequeststeams = FieldProperty(schema.Array(schema.ObjectId))
    teamadmin = FieldProperty(schema.Int)



#   Query Limits.
    homeRecentQuery = FieldProperty(schema.Int)

    def set_password(self, passw):
        self.password = str(bcrypt.hashpw(passw.encode('utf-8'), bcrypt.gensalt
                            ()))

    def register(self, userdict, **kw):
        self.username = userdict["username"]
        self.set_password(userdict["password"])
        self.emailid = userdict["emailid"]
        #self.limit_todo = s.limit_todo
        self.created_todo = 0
        self.account_created = datetime.datetime.now()
        self.teamadmin = 0
        self.numberoflogins = 0

#        Add to Neighborhood database.
        DBSession.flush()
        return self

    def returnprimedetails(self):
        return {
                'username': self.username, 
                'firstname': self.firstname, 
                'lastname': lastname,
                'status': status
            }

    def modify(self, userdict):
        if "username" in userdict:
            self.username = userdict["username"]
        if "emailid" in userdict:
            self.emailid = userdict["emailid"]
        if "firstname" in userdict:
            self.firstname = userdict["firstname"]
        if "lastname" in userdict:
            self.lastname = userdict["lastname"]
        if "organization" in userdict:
            self.organization = userdict["organization"]
        if "status" in userdict:
            self.status = userdict["status"]
        return self

    def get_id(self):
        return self._id

    def isConfirmed(self):
        return self.confirmed

    def createToDoEligible(self):
        if self.limit_todo > self.created_todo:
            return True
        return False

    def updateNextToDo(self, datetime):
        if self.nextToDoDateTime:
            if self.nextToDoDateTime > datetime:
                self.nextToDoDateTime = datetime
        else:
            self.nextToDoDateTime = datetime

    def addToDo(self, todo):
        self.updateNextToDo(todo.todoStartDateTime)
        self._todoitems.append(todo._id)
        if self.created_todo:
            self.created_todo += 1
        else:
            self.created_todo = 1